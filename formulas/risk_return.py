from math import sqrt, prod
from statsmodels.stats.weightstats import DescrStatsW

class RiskReturnEvaluator:
    """
    A utility class for evaluating risk and return metrics for securities and portfolios.

    This class provides methods to calculate:
    - Return on a security (including cash flows)
    - Geometric and arithmetic mean returns
    - Volatility (standard deviation) and annualized volatility
    """

    @staticmethod
    def return_on_security(v0: float, v1: float, cash_flows: float) -> float:
        """
        Calculates the return on a security, accounting for cash flows received during the investment period.

        Args:
            v0: The initial value of the security (price at t=0).
            v1: The value of the security at the end of the investment horizon.
            cash_flows: Cash flows received during the investment period (e.g., dividends, coupons).

        Returns:
            float: The return on investment (ROI) as a decimal (e.g., 0.05 for 5%).
        """
        return ((v1 + cash_flows) / v0) - 1

    @staticmethod
    def geometric_mean_return(returns: list[float]) -> float:
        """
        Calculates the geometric mean return, which represents the average return per period over a multi-period investment.

        Args:
            returns: A list of percentage returns (e.g., [0.05, 0.02, -0.03] for 5%, 2%, -3%).

        Returns:
            float: The geometric mean return as a decimal (e.g., 0.04 for 4%).

        Example:
            >>> returns = [0.05, 0.02, -0.03]  # Returns over 3 periods
            >>> geometric_mean_return(returns)
            0.0128  # Geometric mean return of ~1.28%
        """
        if not returns:
            raise ValueError("The list of returns cannot be empty.")

        growth_factors = [1 + r for r in returns]
        product_of_growth_factors = prod(growth_factors)
        n = len(returns)  # Number of periods is determined by the length of the returns list
        return product_of_growth_factors ** (1 / n) - 1
    @staticmethod
    def annualized_geometric_mean_return(returns: list[float], periods_per_year: int) -> float:
        """
        Calculates the annualized geometric mean return.

        Args:
            returns: A list of percentage returns (e.g., [0.05, 0.02, -0.03] for 5%, 2%, -3%).
            periods_per_year: The number of periods in a year (e.g., 12 for monthly returns).

        Returns:
            float: The annualized geometric mean return as a decimal (e.g., 0.04 for 4%).

        Example:
            >>> returns = [0.01, 0.02, -0.01, 0.03, -0.02]  # Monthly returns
            >>> annualized_geometric_mean_return(returns, periods_per_year=12)
            0.1268  # Annualized geometric mean return of ~12.68%
        """
        geometric_mean = RiskReturnEvaluator.geometric_mean_return(returns)
        return (1 + geometric_mean) ** periods_per_year - 1
    
    @staticmethod
    def arithmetic_mean_return(returns: list[float], probabilities: list[float] = None) -> float:
        """
        Calculates the probability-weighted arithmetic mean return of a security.

        Args:
            returns: A list of returns for each possible outcome.
            probabilities: A list of probabilities corresponding to each return. If None,
                          all returns are assumed to have equal probability. Defaults to None.

        Returns:
            float: The probability-weighted arithmetic mean return as a decimal (e.g., 0.06 for 6%).

        Example:
            >>> returns = [0.10, 0.05, -0.02]  # Possible returns
            >>> probabilities = [0.5, 0.3, 0.2]  # Corresponding probabilities
            >>> arithmetic_mean_return(returns, probabilities)
            0.061  # Weighted mean return of 6.1%
        """
        if probabilities is None:
            # Assume equally weighted probabilities
            probabilities = [1 / len(returns) for _ in range(len(returns))]

        weighted_returns = [probabilities[i] * returns[i] for i in range(len(probabilities))]
        weighted_mean_return = sum(weighted_returns)
        return weighted_mean_return

    @staticmethod
    def volatility(returns: list[float], probabilities: list[float] = None, time_period: int = 1) -> float:
        """
        Calculates the volatility of a security using the weighted standard deviation method,
        scaled to a specific time period using the square root of time rule.

        Args:
            returns: A list of historical returns for the security.
            probabilities: A list of probabilities corresponding to each return. If None,
                          all returns are assumed to have equal probability. Defaults to None.
            time_period: The time period over which to calculate the volatility (e.g., 30 for 30 days).
                        Defaults to 1 (no scaling).

        Returns:
            float: The volatility measure, scaled to the specified time period.

        Example:
            >>> returns = [0.01, 0.02, -0.01, 0.03, -0.02]  # Daily returns
            >>> probabilities = [0.2, 0.2, 0.2, 0.2, 0.2]  # Equal probabilities
            >>> volatility(returns, probabilities, time_period=30)  # 30-day volatility
            0.123  # Example output
        """
        desc_stats = DescrStatsW(returns, weights=probabilities)
        std_dev = desc_stats.std  # Standard deviation of returns
        scaled_volatility = std_dev * sqrt(time_period)  # Scale by square root of time
        return scaled_volatility
    

