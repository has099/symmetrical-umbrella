def calorie_budget_tracker():
    print("=" * 45)
    print("   🏋️‍♂️ برنامج تتبع السعرات اليومية المتبقية")
    print("=" * 45)

    # 1. إدخال الهدف اليومي
    try:
        daily_target = float(input("\n🎯 أدخل هدفك اليومي من السعرات (مثلاً 1800): "))
    except ValueError:
        print("❌ يرجى إدخال رقم صحيح.")
        return

    remaining_calories = daily_target
    total_eaten = 0
    meals = []

    print(f"\n✅ تم تسجيل هدفك: {daily_target:.0f} سعرة حرارية.")
    print("-" * 45)

    # 2. حلقة إدخال الوجبات
    while True:
        print(f"\n📊 الوضع الحالي:")
        print(f"   • السعرات المستهلكة: {total_eaten:.0f} سعرة")
        print(f"   • السعرات المتبقية:  {remaining_calories:.0f} سعرة")
        
        # تحذيرات تلقائية
        if remaining_calories < 0:
            print("⚠️ **تنبيه:** تجاوزت حد السعرات اليومي!")
        elif remaining_calories <= (daily_target * 0.15):
            print("⚠️ **تنبيه:** اقتربت جداً من إنهاء ميزانيتك اليومية!")

        print("\nالخيارات:")
        print("1. إضافة وجبة جديدة 🍎")
        print("2. عرض سجل وجبات اليوم 📜")
        print("3. إنهاء اليوم والخروج 🚪")
        
        choice = input("\nاختر رقم الخيار (1-3): ").strip()

        if choice == "1":
            meal_name = input("اسم الوجبة (مثلاً: بيضتان وسامون): ").strip()
            try:
                cals = float(input(f"سعرات {meal_name}: "))
                meals.append((meal_name, cals))
                total_eaten += cals
                remaining_calories -= cals
                print(f"✔️ تم إضافة ({meal_name}) بـ {cals:.0f} سعرة.")
            except ValueError:
                print("❌ خطأ: يرجى إدخال عدد السعرات كأرقام.")

        elif choice == "2":
            print("\n📜 **سجل وجبات اليوم:**")
            if not meals:
                print("لم تقم بإضافة أي وجبة بعد.")
            else:
                for idx, (name, cals) in enumerate(meals, 1):
                    print(f"   {idx}. {name}: {cals:.0f} سعرة")
                print(f"   -----------------------")
                print(f"   المجموع الكلي: {total_eaten:.0f} سعرة")

        elif choice == "3":
            print("\n✨ **ملخص اليوم النهائي:**")
            print(f"• الهدف الكلي:    {daily_target:.0f} سعرة")
            print(f"• إجمالي ما أكلته: {total_eaten:.0f} سعرة")
            if remaining_calories >= 0:
                print(f"• المتبقي لك:     {remaining_calories:.0f} سعرة (ممتاز! أحسنت الالتزام)")
            else:
                print(f"• الزيادة:        {abs(remaining_calories):.0f} سعرة فوق الهدف")
            print("\nشكراً لاستخدامك البرنامج، بالتوفيق في هدفك الرياضي! 💪")
            break

        else:
            print("❌ خيار غير صحيح، اختر 1 أو 2 أو 3.")


# تشغيل البرنامج
calorie_budget_tracker()
