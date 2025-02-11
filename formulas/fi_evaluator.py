

class FixedIncomeEvaluator:
    """
    A utility class for evaluating fixed-income securities and performing related financial calculations.

    This class provides methods to calculate:
    - Effective annual rate (EAR)
    - Annuity compound and discount factors
    - Bond prices
    - Treasury bill prices and yields
    - Perpetuity prices
    - Annual percentage rate (APR) for Treasury bills

    All methods assume periodic rates and cash flows, unless otherwise specified.
    """
    @staticmethod
    def effective_annual_rate( r: float, n: int) -> float:
        """
        Calculates the effective annual rate (EAR) given a periodic rate and the number of compounding periods.

        Args:
            r: The periodic interest rate (e.g., 0.05 for 5%).
            n: The number of compounding periods in a year.

        Returns:
            float: The effective annual rate as a decimal (e.g., 0.061 for 6.1%).

        Example:
            >>> evaluator = FixedIncomeEvaluator()
            >>> evaluator.effective_annual_rate(0.01, 12)  # 1% monthly rate
            0.1268  # EAR of ~12.68%
        """
        return (1 + r)**n - 1

    @staticmethod
    def annuity_compound_factor( r: float, n: int) -> float:
        """
        Calculates the future value of an ordinary annuity per unit payment.

        Args:
            r: The periodic interest rate (e.g., 0.05 for 5%).
            n: The number of periods.

        Returns:
            float: The annuity compound factor.

        Example:
            >>> evaluator = FixedIncomeEvaluator()
            >>> evaluator.annuity_compound_factor(0.05, 10)  # 5% rate, 10 periods
            12.5779  # Future value factor of ~12.58
        """
        return ((1 + r)**n - 1) / r

    
    def annuity_discount_factor( r: float, n: int) -> float:
        """
        Calculates the present value of an ordinary annuity per unit payment.

        Args:
            r: The periodic discount rate (e.g., 0.05 for 5%).
            n: The number of periods.

        Returns:
            float: The annuity discount factor.

        Example:
            >>> evaluator = FixedIncomeEvaluator()
            >>> evaluator.annuity_discount_factor(0.05, 10)  # 5% rate, 10 periods
            7.7217  # Present value factor of ~7.72
        """
        return (1 - (1 / (1 + r)**n)) / r

    
    def bond_price(self, coupon: float, principal: float, r: float, n: int) -> float:
        """
        Calculates the price of a bond given its coupon, principal, discount rate, and number of periods.

        Args:
            coupon: The periodic coupon payment.
            principal: The principal (face value) of the bond.
            r: The periodic discount rate (e.g., 0.05 for 5%).
            n: The number of periods until maturity.

        Returns:
            float: The price of the bond.

        Example:
            >>> evaluator = FixedIncomeEvaluator()
            >>> evaluator.bond_price(50, 1000, 0.05, 10)  # R50 coupon, R1000 principal, 5% rate, 10 periods
            1000.0  # Bond priced at par
        """
        discount_coupons = coupon * self.annuity_discount_factor(r, n)
        discount_principal = principal / (1 + r)**n
        bond_price = discount_coupons + discount_principal
        return bond_price   

    
    def annuity_price(self, payment: float, r: float, n: int) -> float:
        """
        Calculates the present value of an ordinary annuity.

        Args:
            payment: The periodic payment amount.
            r: The periodic discount rate (e.g., 0.05 for 5%).
            n: The number of periods.

        Returns:
            float: The present value of the annuity.

        Example:
            >>> evaluator = FixedIncomeEvaluator()
            >>> evaluator.annuity_price(100, 0.05, 10)  # R100 payment, 5% rate, 10 periods
            772.17  # Present value of ~R772.17
        """
        return payment * self.annuity_discount_factor(r, n)

    @staticmethod
    def perpetuity_price( cash_flow: float, r: float, g: float = 0) -> float:
        """
        Calculates the price of a perpetuity, optionally accounting for growth.

        Args:
            cash_flow: The periodic cash flow.
            r: The discount rate (e.g., 0.05 for 5%).
            g: The growth rate of the cash flow (default is 0).

        Returns:
            float: The price of the perpetuity.

        Example:
            >>> evaluator = FixedIncomeEvaluator()
            >>> evaluator.perpetuity_price(100, 0.05)  # R100 cash flow, 5% rate
            2000.0  # Price of R2000
        """
        return cash_flow / (r - g)

    @staticmethod
    def treasury_bill_price( principal: float, d: float, D: int) -> float:
        """
        Calculates the price of a Treasury bill using the discount yield method.

        Args:
            principal: The face value of the Treasury bill.
            d: The discount yield (e.g., 0.05 for 5%).
            D: The number of days until maturity.

        Returns:
            float: The price of the Treasury bill.

        Example:
            >>> evaluator = FixedIncomeEvaluator()
            >>> evaluator.treasury_bill_price(1000, 0.02, 90)  # R1000 principal, 2% yield, 90 days
            995.0  # Price of R995
        """
        return principal * (1 - (d * (D / 360)))

    @staticmethod
    def yield_for_treasury_bill( principal: float, price: float) -> float:
        """
        Calculates the yield of a Treasury bill given its principal and price.

        Args:
            principal: The face value of the Treasury bill.
            price: The price of the Treasury bill.

        Returns:
            float: The yield as a decimal (e.g., 0.05 for 5%).

        Example:
            >>> evaluator = FixedIncomeEvaluator()
            >>> evaluator.yield_for_treasury_bill(1000, 995)  # R1000 principal, R995 price
            0.005025  # Yield of ~0.5025%
        """
        return (principal / price) - 1

    @staticmethod
    def apr_for_treasury_bills( r: float, D: int) -> float:
        """
        Calculates the annual percentage rate (APR) for a Treasury bill given its yield and days to maturity.

        Args:
            r: The yield of the Treasury bill (e.g., 0.05 for 5%).
            D: The number of days until maturity.

        Returns:
            float: The APR as a decimal (e.g., 0.05 for 5%).

        Example:
            >>> evaluator = FixedIncomeEvaluator()
            >>> evaluator.apr_for_treasury_bills(0.005, 90)  # 0.5% yield, 90 days
            0.02028  # APR of ~2.028%
        """
        return r * 365 / D


