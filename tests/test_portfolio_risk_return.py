
from formulas.portfolio_risk_return import PortfolioLevelEvaluator
from pytest import fixture



@fixture(scope="function")
def portfolio_evaluator():
    return PortfolioLevelEvaluator()


def test_portfolio_return(portfolio_evaluator):
    probabilities = [0.30, 0.40, 0.30]
    return_on_a = [-0.20, 0.05, 0.40]

    result = portfolio_evaluator.portfolio_return(probabilities, return_on_a)

    assert round(result, 2) == 0.08


def test_covariance_between_a_and_b(portfolio_evaluator):
    return_on_a = [-0.20, 0.05, 0.40]
    return_on_b = [0.10, 0.05, 0.30]

    result = portfolio_evaluator.covariance_between_a_and_b(return_on_a, return_on_b)

    assert round(result, 2) == 0.03

def test_correlation_between_a_and_b(portfolio_evaluator):
    return_on_a = [-0.20, 0.05, 0.40]
    return_on_b = [0.10, 0.05, 0.30]

    result = portfolio_evaluator.correlation_between_a_and_b(return_on_a, return_on_b)
    assert round(result, 2) == 0.82

def test_calculate_portfolio_risk(portfolio_evaluator):
    weights = [0.5, 0.3, 0.2]
    return_of_assets = [[0.05,-0.02,0.03], [0.10, 0.06, 0.08], [0.08, 0.04, 0.06]]

    result = portfolio_evaluator.calculate_portfolio_risk(weights, return_of_assets)

    assert round(result*100,2) == 2.78
    