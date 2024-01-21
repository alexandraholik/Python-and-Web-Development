import pytest
import football_exercise


# The test now works on the class FootballScorer which has the method calculate_points.
# Same parametrization as before, we are just refactoring.
@pytest.mark.parametrize("score_t1, score_t2, points_t1, points_t2", [
    (1, 0, 3, 0),
    (0, 1, 0, 3),
    (1, 1, 1, 1)
])
def test_calculate_points_oop(score_t1, score_t2, points_t1, points_t2):
    fs = football_exercise.FootballScorer('t1', 't2', score_t1, score_t2)
    fs.calculate_points()
    assert fs.points_team_1 == points_t1
    assert fs.points_team_2 == points_t2

# The class can also be initialized by giving the names of the teams and the score.
# Test of the initialization of the class.
# Note that the parametrization is in the form FootballScorer_object, points_t1, points_t2.
@pytest.mark.parametrize('fs, points_t1, points_t2', [
    (football_exercise.FootballScorer('t1', 't2', 0, 0), 1, 1),
    (football_exercise.FootballScorer('t1', 't2', 5, 0), 3, 0),
    (football_exercise.FootballScorer('t1', 't2', 1, 2), 0, 3)
])
def test_init_names_scores(fs, points_t1, points_t2):
    fs.calculate_points()
    assert fs.points_team_1 == points_t1
    assert fs.points_team_2 == points_t2


# A test to catch the exception thrown by the function check_points.
def test_check_input_negative_fails():
    with pytest.raises(ValueError) as e_info:
        football_exercise.FootballScorer('t1', 't2', -1, 0)
    assert str(e_info.value) == 'Invalid Score'
