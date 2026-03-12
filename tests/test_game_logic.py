import pytest

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


# --- check_guess: outcome and return shape ---


def test_winning_guess():
    """Correct guess returns Win and a success message."""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message or "🎉" in message


def test_guess_too_high():
    """Guess above secret returns outcome 'Too High'."""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    """Guess below secret returns outcome 'Too Low'."""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1 fix: hint direction (was reversed: said "go higher" when secret was lower, etc.) ---


def test_hint_when_guess_too_high_says_go_lower():
    """When guess is too high, hint must tell player to go LOWER (bug fix: was incorrectly 'Go HIGHER!')."""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper(), "Hint must direct player to go lower when guess is too high"


def test_hint_when_guess_too_low_says_go_higher():
    """When guess is too low, hint must tell player to go HIGHER (bug fix: was incorrectly 'Go LOWER!')."""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper(), "Hint must direct player to go higher when guess is too low"


def test_hint_direction_with_str_secret_typeerror_path():
    """Hint direction is correct even when secret is str (TypeError branch). Bug 1 fix in except block."""
    # Even-numbered attempts in app pass secret as str; hint direction must still be correct
    outcome_low, message_low = check_guess(40, "50")
    outcome_high, message_high = check_guess(60, "50")
    assert outcome_low == "Too Low" and "HIGHER" in message_low.upper()
    assert outcome_high == "Too High" and "LOWER" in message_high.upper()


# --- get_range_for_difficulty (used for attempt limit and new game range) ---


def test_get_range_easy():
    """Easy difficulty uses 1–20 range."""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20


def test_get_range_normal():
    """Normal difficulty uses 1–100 range."""
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100


def test_get_range_hard():
    """Hard difficulty uses 1–50 range."""
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 50


# --- parse_guess ---


def test_parse_guess_valid_integer():
    """Valid integer string parses to (True, int, None)."""
    ok, value, err = parse_guess("42")
    assert ok is True and value == 42 and err is None


def test_parse_guess_empty_returns_error():
    """Empty input returns error (Bug 3 context: validation before counting attempt)."""
    ok, value, err = parse_guess("")
    assert ok is False and value is None and "Enter" in err


def test_parse_guess_non_number_returns_error():
    """Non-numeric input returns error."""
    ok, value, err = parse_guess("abc")
    assert ok is False and value is None and err is not None


# --- update_score ---


def test_update_score_win_gives_positive_points():
    """Winning adds points to score."""
    new_score = update_score(0, "Win", 0)
    assert new_score > 0


def test_update_score_too_high_or_low_can_reduce():
    """Too High / Too Low can reduce score."""
    new_score = update_score(10, "Too Low", 1)
    assert new_score <= 10
