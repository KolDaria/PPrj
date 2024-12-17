from src.masks import get_mask_account, get_mask_card_number

result1 = get_mask_card_number(7000245654872839)
result2 = get_mask_account(73654108430135874305)

print(result1)
print(result2)
