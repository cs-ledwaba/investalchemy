import pytest
from formulas.risk_return import RiskReturnEvaluator

# Create an instance of the class
evaluator = RiskReturnEvaluator()

@pytest.mark.parametrize("returns, expected", [
    ([-0.1, 0.20, 0.3], 0.1198),  # Mixed returns
    ([0.05, 0.02, -0.03], 0.0128),  # Small returns
    ([0.0, 0.0, 0.0], 0.0),  # Zero returns
])
def test_geometric_mean_return(returns, expected):
    """
    Test the geometric_mean_return method with various inputs.
    """
    result = evaluator.geometric_mean_return(returns)
    assert round(result, 4) == expected


def test_arithmetic_mean_return_with_equal_probabilities():
    """
    Test the arithmetic_mean_return method with equal probabilities.
    """
    returns = [-0.1, 0.20, 0.3]
    expected_ans = 0.1333
    result = evaluator.arithmetic_mean_return(returns)
    assert round(result, 4) == expected_ans


def test_arithmetic_mean_return_with_given_probabilities():
    """
    Test the arithmetic_mean_return method with given probabilities.
    """
    probabilities = [0.30, 0.40, 0.30]
    returns = [0.10, 0.05, 0.30]
    expected_ans = 0.14
    result = evaluator.arithmetic_mean_return(returns, probabilities)
    assert result == expected_ans


def test_volatility_with_given_probabilities():
    """
    Test the volatility method with given probabilities.
    """
    probabilities = [0.30, 0.40, 0.30]
    returns = [0.10, 0.05, 0.30]
    expected_ans = 0.1068
    result = evaluator.volatility(returns, probabilities)
    assert round(result, 4) == expected_ans


# def test_annualized_volatility():
#     """
#     Test the annualized_volatility method with monthly volatility.
#     """
#     monthly_volatility = 0.05
#     expected_ans = 0.1732
#     result = evaluator.vol(monthly_volatility, time_period=12)
#     assert round(result, 4) == expected_ans