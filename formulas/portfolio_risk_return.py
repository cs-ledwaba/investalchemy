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
    def portfolio_return(weights: list[float], returns: list[float]) -> float:
        """
        Calculates the return of a portfolio using the weighted average of the asset returns.
        Args:
            weights: The weights of the assets in the portfolio.
            returns: The returns of the assets in the portfolio.
        Returns:
            float: The portfolio return as a decimal (e.g., 0.06 for 6%).
        """
        return np.dot(weights, returns)
    
    @staticmethod
    def covariance_between_a_and_b(returns_asset_a: list[float], returns_asset_b: list[float]) -> np.ndarray:
        """
        Calculates the covariance between the returns of two assets.
        Args:
            returns_asset_a: The returns of the first asset.
            returns_asset_b: The returns of the second asset.
        Returns:
            np.ndarray: The covariance value.
        """
        return np.cov(returns_asset_a, returns_asset_b)[0][1]
    @staticmethod
    def correlation_between_a_and_b(returns_asset_a: list[float], returns_asset_b: list[float]) -> float:
        """
        Calculates the correlation between the returns of two assets.
        Args:
            returns_asset_a: The returns of the first asset.
            returns_asset_b: The returns of the second asset.
        Returns:
            float: The correlation coefficient.
        """
        return np.corrcoef(returns_asset_a, returns_asset_b)[0][1]
    @staticmethod
    def calculate_portfolio_risk(weights: list[float], return_of_assets: list[list[float]]) -> float:
        """
        Calculates the risk (standard deviation) of a portfolio.
        Args:
            weights: The weights of the assets in the portfolio.
            return_of_assets: The returns of the assets in the portfolio.
        Returns:
            float: The portfolio risk (standard deviation).
        """
        covariance_matrix = np.cov(np.array(return_of_assets))
        variance = np.dot(weights, np.dot(covariance_matrix, weights))
        return np.sqrt(variance)