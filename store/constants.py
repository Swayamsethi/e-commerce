# User Roles
USER_ROLE = (
    (1,"ADMIN"),
    (2,"CUSTOMER"),
    (3,"SELLER")
)
ADMIN = 1
CUSTOMER = 2
SELLER = 3

# Payment Options
PAYMENT_OPTION =(
    (1,"UPI"),
    (2,"ATM CARD"),
    (3,"NETBANKING"),
    (4,"WALLETS"),
    (5,"CASH_ON_DELIVERY"),
    (6,"GIFT CARDS")
)
CASH_ON_DELIVERY= 3

# Order History
ORDER_HISTORY_STATUS =(
    (1,"DELIVERED"),
    (2,"RETURNED"),
    (3,"REPLACED")
)
DELIVERED= 1


# Payment Status
PAYMENT_STATUS =(
    (1,"COMPLETED"),
    (2,"PENDING"),
    (3,"FAILED")
)
PENDING= 2

# Gender
GENDER =(
    (1,"MALE"),
    (2,"FEMALE"),
    (3,"OTHER")
)

# Order status
ORDER_STATUS =(
    (1,"SUCESS"),
    (2,"FAIL"),
    (3,"PROCESSING")
)
PROCESSING=3