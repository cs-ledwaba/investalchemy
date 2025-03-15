class EquityEvaluator:
    """
    A utility class for evaluating equity investments and performing related financial
    calculations.

    This class provides methods to calculate:
    - Total return on a stock (including capital gains and dividends)
    - Stock valuation using Dividend Discount Model (DDM) and Gordon Growth Model
    - Price-to-Earnings (P/E) ratio and earnings yield
    - Dividend yield
    - Net Present Value (NPV) of cash flows
    """

    @staticmethod
    def return_on_stock(
        initial_price: float, current_price: float, dividend_payment: float
    ) -> float:
        """
        Calculates the total return on a stock, including capital gains and dividend
        yield.

        Args:
            initial_price: The initial price of the stock.
            current_price: The current price of the stock.
            dividend_payment: The total dividend payment received during the holding
                              period.

        Returns:
            float: The total return as a percentage (e.g., 10.5 for 10.5%).

        Example:
            >>> EquityEvaluator.return_on_stock(100, 120, 5)
                # Initial price R100, current price R120, dividend R5
                25.0  # Total return of 25%
        """
        capital_gains = (current_price - initial_price) / initial_price
        dividend_yield = dividend_payment / initial_price
        total_return = (capital_gains + dividend_yield) * 100
        return total_return

    @staticmethod
    def stock_valuation_dividend_discount_model(
        dividend_payment: float, r: float, t: int
    ) -> float:
        """
        Calculates the present value of a stock using the Dividend Discount Model (DDM).

        Args:
            dividend_payment: The expected annual dividend payment.
            r: The discount rate (e.g., 0.05 for 5%).
            t: The number of years for which dividends are expected.

        Returns:
            float: The present value of the stock.

        Example:
            >>> EquityEvaluator.stock_valuation_dividend_discount_model(5, 0.05, 10)
                # R5 dividend, 5% rate, 10 years
                38.61  # Present value of ~R38.61
        """
        price = 0
        for i in range(1, t + 1):
            price += dividend_payment / (1 + r) ** i
        return price

    @staticmethod
    def gordon_growth_model(dividend_payment: float, r: float, g: float) -> float:
        """
        Calculates the present value of a stock using the Gordon Growth Model.

        Args:
            dividend_payment: The expected annual dividend payment.
            r: The discount rate (e.g., 0.05 for 5%).
            g: The expected growth rate of dividends (e.g., 0.02 for 2%).

        Returns:
            float: The present value of the stock.

        Example:
            >>> EquityEvaluator.gordon_growth_model(5, 0.05, 0.02)
                # R5 dividend, 5% rate, 2% growth
                166.67  # Present value of ~R166.67
        """
        if r <= g:
            raise ValueError("Discount rate (r) must be greater than growth rate (g).")
        return dividend_payment / (r - g)

    @staticmethod
    def price_to_earnings_ratio(price: float, earnings_per_share: float) -> float:
        """
        Calculates the Price-to-Earnings (P/E) ratio of a stock.

        Args:
            price: The current price of the stock.
            earnings_per_share: The earnings per share (EPS) of the stock.

        Returns:
            float: The P/E ratio.

        Example:
            >>> EquityEvaluator.price_to_earnings_ratio(100, 5)  # Price R100, EPS R5
            20.0  # P/E ratio of 20
        """
        if earnings_per_share <= 0:
            raise ValueError("Earnings per share must be positive.")
        return price / earnings_per_share

    @staticmethod
    def earnings_yield(price: float, earnings_per_share: float) -> float:
        """
        Calculates the earnings yield of a stock.

        Args:
            price: The current price of the stock.
            earnings_per_share: The earnings per share (EPS) of the stock.

        Returns:
            float: The earnings yield as a decimal (e.g., 0.05 for 5%).

        Example:
            >>> EquityEvaluator.earnings_yield(100, 5)  # Price R100, EPS R5
            0.05  # Earnings yield of 5%
        """
        if earnings_per_share <= 0:
            raise ValueError("Earnings per share must be positive.")
        return earnings_per_share / price

    @staticmethod
    def dividend_yield(dividend_payment: float, price: float) -> float:
        """
        Calculates the dividend yield of a stock.

        Args:
            dividend_payment: The annual dividend payment.
            price: The current price of the stock.

        Returns:
            float: The dividend yield as a decimal (e.g., 0.03 for 3%).

        Example:
            >>> EquityEvaluator.dividend_yield(3, 100)  # Dividend R3, price R100
            0.03  # Dividend yield of 3%
        """
        if price <= 0:
            raise ValueError("Price must be positive.")
        return dividend_payment / price

    @staticmethod
    def net_present_value(cash_flows: list[float], r: float) -> float:
        """
        Calculates the Net Present Value (NPV) of a series of cash flows.

        Args:
            cash_flows: A list of cash flows (e.g., [-100, 50, 60, 70] for an initial
                        investment of R100).
            r: The discount rate (e.g., 0.05 for 5%).

        Returns:
            float: The NPV of the cash flows.

        Example:
            >>> EquityEvaluator.net_present_value([-100, 50, 60, 70], 0.05)
                # Initial investment R100, cash flows R50, R60, R70
                64.47  # NPV of ~R64.47
        """
        npv = 0
        for t, cash_flow in enumerate(cash_flows):
            npv += cash_flow / (1 + r) ** t
        return npv
