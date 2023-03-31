def solve(chicken_num, rabbit_num, total_num):
    """计算鸡兔同笼问题的函数"""
    for chicken in range(total_num + 1):
        rabbit = total_num - chicken
        if 2 * chicken + 4 * rabbit == rabbit_num:
            if chicken + rabbit == chicken_num:
                return chicken, rabbit。
    return None
