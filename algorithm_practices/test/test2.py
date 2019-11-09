input_args = input('数値を入力してね！:')

if input_args.isdecimal():
    args = int(input_args)
    if args <= 10:
        print('10以下です')
    else:
        print('10より大きいです')
else:
    print('数値を入力してください')