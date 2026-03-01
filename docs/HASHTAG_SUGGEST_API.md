# Hashtag suggestion API

Автоматическая подсказка хештегов при создании вопроса через Google Gemini.

## Endpoint

```
POST /api/hashtags/pick
```

**Auth:** Bearer token (обязательно)

**Request body:**
```json
{
  "question_text": "What is your favorite programming language?",
  "options": ["Python", "JavaScript", "Go", "Rust"]
}
```

- `question_text` (string) — текст вопроса
- `options` (array of string) — варианты ответов (опционально)

**Response:**
```json
{
  "hashtags": ["Coding", "Programming", "Technology"]
}
```

Возвращает 1–10 релевантных хештегов из существующего списка в БД.

## Настройка

1. Добавьте `GOOGLE_API_KEY` в `.env` (ключ из [Google AI Studio](https://aistudio.google.com/apikey))
2. Без ключа endpoint возвращает `{"hashtags": []}`

## Интеграция на фронтенде

1. **Триггер:** после ввода первого слова в поле вопроса (debounce 300–500 ms)
2. **Вызов:** при каждом изменении текста/опций — `POST /api/hashtags/pick` с текущими данными
3. **Отображение:** показать предложенные хештеги как chips/теги, пользователь может добавить или проигнорировать

Пример (псевдокод):

```javascript
// Debounce 400ms
const suggestHashtags = debounce(async (questionText, options) => {
  if (!questionText.trim()) return [];
  const res = await fetch('/api/hashtags/pick', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      question_text: questionText,
      options: options.map(o => o.text),
    }),
  });
  const { hashtags } = await res.json();
  return hashtags;
}, 400);

// При вводе вопроса
onQuestionChange((text, options) => {
  if (text.split(/\s+/).length >= 1) {
    suggestHashtags(text, options).then(setSuggestedHashtags);
  }
});
```
