# Name:
# Email ID:
    
def get_min_allocation(rating):
    bonus = [1] * len(rating)
    for i in range(1, len(rating)):
        if rating[i] > rating[i - 1]:
            bonus[i] = bonus[i - 1] + 1

    for i in range(len(rating) - 2, -1, -1):
        if rating[i] > rating[i + 1]:
            bonus[i] = max(bonus[i], bonus[i + 1] + 1)
    return bonus


# def get_min_allocation(rating):
#     # Modify the code below.
#     bonus = []
#     for r in rating:
#         bonus.append(1)
        
#     for i in range(len(rating)):
#         current_rating = rating[i]
#         if i == 0:
#             if len(rating) > 2:
#                 right_n = rating[i+1]
#                 if right_n < current_rating:
#                     bonus[i] += 1
#         elif i == len(rating) - 1:
#             left_n = rating[i - 1]
#             if current_rating > left_n:
#                 bonus[i] += max(1, bonus[i - 1])
#         else:
#             left_n = rating[i - 1]
#             right_n = rating[i+1]
#             if current_rating > left_n:
#                 bonus[i] += max(1, bonus[i - 1])
#                 continue
#             if current_rating > right_n:
#                 bonus[i] += max(1, bonus[i + 1])
#                 continue
#     return bonus