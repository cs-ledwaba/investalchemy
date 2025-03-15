from pytest import fixture

from investalchemy.portfolio_risk_return import PortfolioLevelEvaluator


@fixture(scope="function")
def portfolio_evaluator():
    return PortfolioLevelEvaluator()


def test_portfolio_return(portfolio_evaluator):
    probabilities = [0.30, 0.40, 0.30]
    return_on_a = [-0.20, 0.05, 0.40]

    result = portfolio_evaluator.calculate_portfolio_return(probabilities, return_on_a)

    assert round(result, 2) == 0.08


def test_covariance_matrix_with_2_assets(portfolio_evaluator):
    return_on_a = [-0.20, 0.05, 0.40]
    return_on_b = [0.10, 0.05, 0.30]
    returns = [return_on_a, return_on_b]

    result = portfolio_evaluator.calculate_covariance_matrix(returns)

    assert round(result[0][1], 2) == 0.03


def test_correlation_matrix_with_2_assets(portfolio_evaluator):
    return_on_a = [-0.20, 0.05, 0.40]
    return_on_b = [0.10, 0.05, 0.30]
    returns = [return_on_a, return_on_b]
    result = portfolio_evaluator.calculate_correlation_matrix(returns)
    assert round(result[0][1], 2) == 0.82


def test_calculate_portfolio_risk(portfolio_evaluator):
    weights = [0.5, 0.3, 0.2]
    return_of_assets = [[0.05, -0.02, 0.03], [0.10, 0.06, 0.08], [0.08, 0.04, 0.06]]

    result = portfolio_evaluator.calculate_portfolio_risk(weights, return_of_assets)

    assert round(result * 100, 2) == 2.78
