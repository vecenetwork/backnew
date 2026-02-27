from enum import Enum


class FeedTypeEnum(str, Enum):
    """Type of feed to retrieve."""
    default = "default"
    me = "me"
    other = "other"


class SortOrderEnum(str, Enum):
    """Sorting order for queries."""
    asc = "asc"
    desc = "desc"


class SortByEnum(str, Enum):
    """Fields that can be used for sorting."""
    created_at = "created_at"


class UserRoleEnum(str, Enum):
    """User's role in relation to a question (for filtering)."""
    all = "all"
    author = "author"
    respondent = "respondent" 