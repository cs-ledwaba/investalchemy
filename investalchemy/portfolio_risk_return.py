import numpy as np


class PortfolioLevelEvaluator:
    """
    A utility class for evaluating risk and return metrics for portfolios.
    This class provides methods to calculate:
    - Return on a portfolios
    - Covariance between two assets
    - Correlation between two assets
    - Volatility (standard deviation)
    """

    @staticmethod
    def calculate_portfolio_return(weights: list[float], returns: list[float]) -> float:
        """
        Calculates the return of a portfolio using the weighted average of the asset
        returns.
        Args:
            weights: The weights of the assets in the portfolio.
            returns: The returns of the assets in the portfolio.
        Returns:
            float: The portfolio return as a decimal (e.g., 0.06 for 6%).
        """
        return np.dot(weights, returns)

    @staticmethod
    def calculate_covariance_matrix(return_of_assets: list[list[float]]) -> np.ndarray:
        """
        Calculates the covariance matrix of asset returns.
        Args:
            return_of_assets: The returns of the assets in the portfolio.
        Returns:
            np.ndarray: The covariance matrix.
        """
        return np.cov(np.array(return_of_assets))

    @staticmethod
    def calculate_correlation_matrix(return_of_assets: list[list[float]]) -> np.ndarray:
        """
        Calculates the covariance matrix of asset returns.
        Args:
            return_of_assets: The returns of the assets in the portfolio.
        Returns:
            np.ndarray: The covariance matrix.
        """
        return np.corrcoef(np.array(return_of_assets))

    @staticmethod
    def calculate_portfolio_risk(
        weights: list[float], return_of_assets: list[list[float]]
    ) -> float:
        """
        Calculates the risk (standard deviation) of a portfolio.
        Args:
            weights: The weights of the assets in the portfolio.
            return_of_assets: The returns of the assets in the portfolio.
        Returns:
            float: The portfolio risk (standard deviation).
        """
        covariance_matrix = PortfolioLevelEvaluator.calculate_covariance_matrix(
            return_of_assets
        )
        variance = np.dot(weights, np.dot(covariance_matrix, weights))
        return np.sqrt(variance)
