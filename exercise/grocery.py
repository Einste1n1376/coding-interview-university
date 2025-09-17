def main():
    d = {}
    while True:
        try:
            input_items = input().upper()
            if input_items in d:
                d[input_items] += 1
            else:
                d[input_items] = 1

        except EOFError:
            # 按字母顺序排序字典的键
            for key in sorted(d.keys()):
                print(f"{d[key]} {key}")
            break

if __name__ == "__main__":
    main()