while True:

    print("Выбери опцию:")
    print("1 — Конвертер длин")
    print("2 — Конвертер масс")
    print("3 — Выход")
    option = input("Твой выбор: ").strip()

    if option == "1":
        print("Введи единицу длины")
        choice = input("Твой выбор: ").strip().lower()
    
        if choice in ("миллиметры", "мм", "миллиметр"):
            while True:
                try:
                    мм = float(input("Введите длину в миллиметрах: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            см = мм/10
            дм = мм/100
            м = мм/1000
            км = мм/1000000
            IN = мм/25.4
            FT = мм/304.8
            YD = мм/914.4
            MI = мм/1609344
            print("Сантиметры:", см)
            print("Дециметры:", дм)
            print("Метры:", м)
            print("Километры:", км)
            print("Дюймы:", round(IN, 6))
            print("Футы:", round(FT, 6))
            print("Ярды:", round(YD, 6))
            print("Мили:", round(MI, 6))

        elif choice in ("сантиметры", "см", "сантиметр"):
            while True:
                try:
                    см = float(input("Введите длину в сантиметрах: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            мм = см*10
            дм = см/10
            м = см/100
            км = см/100000
            IN = см/2.54
            FT = см/30.48
            YD = см/91.44
            MI = см/160934.4
            print("Миллиметры:", мм)
            print("Дециметры:", дм)
            print("Метры:", м)
            print("Километры:", км)
            print("Дюймы:", round(IN, 6))
            print("Футы:", round(FT, 6))
            print("Ярды:", round(YD, 6))
            print("Мили:", round(MI, 6))
        
        elif choice in ("дециметры", "дм", "дециметр"):
            while True:
                try:
                    дм = float(input("Введите длину в дециметрах: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            мм = дм*100
            см = дм*10
            м = дм/10
            км = дм/10000
            IN = дм*3.937007
            FT = дм/3.048
            YD = дм/9.144
            MI = дм/16093.44
            print("Миллиметры:", мм)
            print("Сантиметры:", см)
            print("Метры:", м)
            print("Километры:", км)
            print("Дюймы:", round(IN, 6))
            print("Футы:", round(FT, 6))
            print("Ярды:", round(YD, 6))
            print("Мили:", round(MI, 6))
        
        elif choice in ("метры", "м", "метр"):
            while True:
                try:
                    м = float(input("Введите длину в метрах: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            мм = м*1000
            см = м*100
            дм = м*10
            км = м/1000
            IN = м*39.370078
            FT = м*3.28084
            YD = м*1.09361
            MI = м/1609.344
            print("Миллиметры:", мм)
            print("Сантиметры:", см)
            print("Дециметры:", дм)
            print("Километры:", км)
            print("Дюймы:", round(IN, 6))
            print("Футы:", round(FT, 6))
            print("Ярды:", round(YD, 6))
            print("Мили:", round(MI, 6))
    
        elif choice in ("километры", "км", "километр"):
            while True:
                try:
                    км = float(input("Введите длину в километрах: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            мм = км*1000000
            см = км*100000
            дм = км*10000
            м = км*1000
            IN = км*39370.078740
            FT = км*3280.839895
            YD = км*1093.613298
            MI = км/1.609344
            print("Миллиметры:", мм)
            print("Сантиметры:", см)
            print("Дециметры:", дм)
            print("Метры:", м)
            print("Дюймы:", round(IN, 6))
            print("Футы:", round(FT, 6))
            print("Ярды:", round(YD, 6))
            print("Мили:", round(MI, 6))
    
        elif choice in ("дюймы", "in", "дюйм"):
            while True:
                try:
                    IN = float(input("Введите длину в дюймах: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            мм = IN*25.4
            см = IN*2.54
            дм = IN/3.937007
            м = IN/39.370078
            км = IN/39370.078740
            FT = IN/12
            YD = IN/36
            MI = IN/63360
            print("Миллиметры:", round(мм, 6))
            print("Сантиметры:", round(см, 6))
            print("Дециметры:", round(дм, 6))
            print("Метры:", round(м, 6))
            print("Километры:", round(км, 6))
            print("Футы:", round(FT, 6))
            print("Ярды:", round(YD, 6))
            print("Мили:", round(MI, 6))
    
        elif choice in ("футы", "ft", "фут"):
            while True:
                try:
                    FT = float(input("Введите длину в футах: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            мм = FT*304.8
            см = FT*30.48
            дм = FT*3.048
            м = FT/3.28084
            км = FT/3280.839895
            IN = FT*12
            YD = FT/3
            MI = FT/5280
            print("Миллиметры:", round(мм, 6))
            print("Сантиметры:", round(см, 6))
            print("Дециметры:", round(дм, 6))
            print("Метры:", round(м, 6))
            print("Километры:", round(км, 6))
            print("Дюймы:", round(IN, 6))
            print("Ярды:", round(YD, 6))
            print("Мили:", round(MI, 6))
    
        elif choice in ("ярды", "yd", "ярд"):
            while True:
                try:
                    YD = float(input("Введите длину в ярдах: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            мм = YD*914.4
            см = YD*91.44
            дм = YD*9.144
            м = YD/1.09361
            км = YD/1093.613298
            IN = YD*36
            FT = YD*3
            MI = YD/1760
            print("Миллиметры:", round(мм, 6))
            print("Сантиметры:", round(см, 6))
            print("Дециметры:", round(дм, 6))
            print("Метры:", round(м, 6))
            print("Километры:", round(км, 6))
            print("Дюймы:", round(IN, 6))
            print("Футы:", round(FT, 6))
            print("Мили:", round(MI, 6))
    
        elif choice in ("мили", "mi", "миля"):
            while True:
                try:
                    MI = float(input("Введите длину в милях: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            мм = MI*1609344
            см = MI*160934.4
            дм = MI*16093.44
            м = MI*1609.344
            км = MI*1.609344
            IN = MI*63360
            FT = MI*5280
            YD = MI*1760
            print("Миллиметры:", round(мм, 6))
            print("Сантиметры:", round(см, 6))
            print("Дециметры:", round(дм, 6))
            print("Метры:", round(м, 6))
            print("Километры:", round(км, 6))
            print("Дюймы:", round(IN, 6))
            print("Футы:", round(FT, 6))
            print("Ярды:", round(YD, 6))
        
        else:
            print("Неправильный выбор")
        
    if option == "2":
        print("Введи единицу массы")
        choice = input("Твой выбор: ").strip().lower()
    
        if choice in ("граммы", "гр", "г", "грамм"):
            while True:
                try:
                    гр = float(input("Введите массу в граммах: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            кг = гр/1000
            ц = гр/100000
            т = гр/1000000
            OZ = гр/28.349523
            LB = гр/453.59237
            print("Килограммы:", кг)
            print("Центнеры:", ц)
            print("Тонны:", т)
            print("Унции:", round(OZ, 6))
            print("Фунты:", round(LB, 6))

        elif choice in ("килограммы", "кг", "килограмм"):
            while True:
                try:
                    кг = float(input("Введите массу в килограммах: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            гр = кг*1000
            ц = кг/100
            т = кг/1000
            OZ = кг*35.273961
            LB = кг*2.204622
            print("Граммы:", гр)
            print("Центнеры:", ц)
            print("Тонны:", т)
            print("Унции:", round(OZ, 6))
            print("Фунты:", round(LB, 6))

        elif choice in ("центнеры", "ц", "центнер"):
            while True:
                try:
                    ц = float(input("Введите массу в центнерах: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            гр = ц*100000
            кг = ц*100
            т = ц/10
            OZ = ц*3527.396
            LB = ц*220.462262
            print("Граммы:", гр)
            print("Килограммы:", кг)
            print("Тонны:", т)
            print("Унции:", round(OZ, 6))
            print("Фунты:", round(LB, 6))

        elif choice in ("тонны", "т", "тонна"):
            while True:
                try:
                    т = float(input("Введите массу в тоннах: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            гр = т*1000000
            кг = т*1000
            ц = т*10
            OZ = т*35273.961949
            LB = т*2204.622621
            print("Граммы:", гр)
            print("Килограммы:", кг)
            print("Центнеры:", ц)
            print("Унции:", round(OZ, 6))
            print("Фунты:", round(LB, 6))
    
        elif choice in ("унции", "oz", "унция"):
            while True:
                try:
                    OZ = float(input("Введите массу в унциях: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            гр = OZ*28.349523
            кг = OZ/35.273961
            ц = OZ/3527.396
            т = OZ/35273.961949
            LB = OZ/16
            print("Граммы:", round(гр, 6))
            print("Килограммы:", round(кг, 6))
            print("Центнеры:", round(ц, 6))
            print("Тонны:", round(т, 6))
            print("Фунты:", round(LB, 6))
    
        elif choice in ("фунты", "lb", "фунт"):
            while True:
                try:
                    LB = float(input("Введите массу в фунтах: "))
                    break
                except ValueError:
                    print("Ошибка: введите число!")
            гр = LB*453.59237
            кг = LB/2.204622
            ц = LB/220.462262
            т = LB/2204.622621
            OZ = LB*16
            print("Граммы:", round(гр, 6))
            print("Килограммы:", round(кг, 6))
            print("Центнеры:", round(ц, 6))
            print("Тонны:", round(т, 6))
            print("Унции:", round(OZ, 6))
    
        else:
            print("Неправильный выбор")
        
    if option == "3":
        break