# Transformer-Calculator
import math

print("=" * 50)
print("          TRANSFORMER CALCULATOR")
print("=" * 50)

print("\nSelect calculation:")
print("1. Calculate Secondary Voltage")
print("2. Calculate Secondary Current")
print("3. Calculate Turns Ratio")
print("4. Calculate Transformer Efficiency")
print("5. Calculate Apparent Power")

choice = int(input("\nEnter your choice (1-5): "))

if choice == 1:
    # Secondary voltage
    vp = float(input("Enter primary voltage (V): "))
    np = float(input("Enter primary turns: "))
    ns = float(input("Enter secondary turns: "))

    vs = vp * (ns / np)

    print("\n--- Result ---")
    print(f"Primary Voltage   : {vp:.2f} V")
    print(f"Primary Turns     : {np:.0f}")
    print(f"Secondary Turns   : {ns:.0f}")
    print(f"Secondary Voltage : {vs:.2f} V")


elif choice == 2:
    # Secondary current
    vp = float(input("Enter primary voltage (V): "))
    ip = float(input("Enter primary current (A): "))
    vs = float(input("Enter secondary voltage (V): "))

    apparent_power = vp * ip
    isec = apparent_power / vs

    print("\n--- Result ---")
    print(f"Primary Voltage   : {vp:.2f} V")
    print(f"Primary Current   : {ip:.2f} A")
    print(f"Secondary Voltage : {vs:.2f} V")
    print(f"Secondary Current : {isec:.2f} A")


elif choice == 3:
    # Turns ratio
    np = float(input("Enter primary turns: "))
    ns = float(input("Enter secondary turns: "))

    turns_ratio = np / ns

    print("\n--- Result ---")
    print(f"Primary Turns     : {np:.0f}")
    print(f"Secondary Turns   : {ns:.0f}")
    print(f"Turns Ratio       : {turns_ratio:.2f}:1")

    if turns_ratio > 1:
        print("Transformer Type  : Step-Down")

    elif turns_ratio < 1:
        print("Transformer Type  : Step-Up")

    else:
        print("Transformer Type  : 1:1 Transformer")


elif choice == 4:
    # Efficiency
    input_power = float(input("Enter input power (W): "))
    output_power = float(input("Enter output power (W): "))

    if output_power > input_power:
        print("\nError: Output power cannot exceed input power.")

    else:
        efficiency = (output_power / input_power) * 100
        losses = input_power - output_power

        print("\n--- Result ---")
        print(f"Input Power      : {input_power:.2f} W")
        print(f"Output Power     : {output_power:.2f} W")
        print(f"Power Loss       : {losses:.2f} W")
        print(f"Efficiency       : {efficiency:.2f} %")


elif choice == 5:
    # Apparent power
    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (A): "))

    apparent_power = voltage * current

    print("\n--- Result ---")
    print(f"Voltage          : {voltage:.2f} V")
    print(f"Current          : {current:.2f} A")
    print(f"Apparent Power   : {apparent_power:.2f} VA")


else:
    print("\nInvalid choice. Please select 1 to 5.")

print("\n" + "=" * 50)
print("           CALCULATION COMPLETED")
print("=" * 50)
