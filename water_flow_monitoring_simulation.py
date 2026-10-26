import time

# --- SIMULATED HARDWARE VARIABLES ---
last_flow_status = False  # False = stopped, True = flowing


def get_simulated_flow_rate(start_time):
    """
    Simulates water flow based on elapsed time.
    0 - 5 sec  : Water OFF (0.0 L/min)
    5 - 15 sec : Water ON  (5.0 L/min)
    15+ sec    : Water OFF (0.0 L/min)
    """
    elapsed = time.time() - start_time

    if 5 <= elapsed <= 15:
        return 5.0  # Simulated 5 Litres/Minute
    else:
        return 0.0  # No flow


def alert_flow_start():
    print("\n--------------------------------------------------")
    print("ALERT: Water Started Flowing! (BEEP: 1.5s Long Sound)")
    print("--------------------------------------------------\n")


def alert_flow_stop():
    print("\n--------------------------------------------------")
    print("ALERT: Water Stopped Flowing! (BEEP: Beep.. Beep.. Beep..)")
    print("--------------------------------------------------\n")


def main():
    global last_flow_status

    print("==================================================")
    print("        WATER FLOW MONITORING SIMULATION          ")
    print("==================================================")
    print("0 - 5 sec  : Water OFF (No Flow)")
    print("5 - 15 sec : Water ON  (Flow Rate ~5.0 L/min)")
    print("15+ sec    : Water OFF (Flow Stopped)")
    print("==================================================\n")

    start_time = time.time()

    try:
        while True:
            # Get flow rate every 1 second
            flow_rate = get_simulated_flow_rate(start_time)

            print(f"[STATUS] Current Flow Rate: {flow_rate:.2f} L/min")

            # --- SOUND LOGIC FOR FLOW START & STOP ---

            # 1. Water JUST STARTED flowing
            if flow_rate >= 0.5 and not last_flow_status:
                alert_flow_start()
                last_flow_status = True

            # 2. Water JUST STOPPED flowing
            elif flow_rate < 0.5 and last_flow_status:
                alert_flow_stop()
                last_flow_status = False

            # Wait for 1 second before next check
            time.sleep(1.0)

    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")


if __name__ == "__main__":
    main()
