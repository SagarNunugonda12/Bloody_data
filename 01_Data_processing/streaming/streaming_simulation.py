import time
import sys

print("=== [STREAMING] Live Data Pipeline Activated ===")
print("Pipeline is listening continuously... Press Ctrl+C anytime to stop.\n")

# Stream variables stay open in memory
running_revenue = 0.0
event_count = 0

try:
    while True:
        # Simulate waiting for an incoming streaming event
        print("⚡ Waiting for incoming order transaction...")
        user_input = input("Enter new order amount (or leave blank to pass a second): ").strip()
        
        if user_input:
            try:
                # An event arrived!
                order_amount = float(user_input)
                running_revenue += order_amount
                event_count += 1
                
                # Immediate processing and output update
                print(f"\n[EVENT DETECTED] Processed 1 transaction worth ₹{order_amount:,.2f}")
                print(f"📈 [REAL-TIME DASHBOARD] Total Events: {event_count} | Running Revenue: ₹{running_revenue:,.2f}")
                print("-" * 50)
            except ValueError:
                print("❌ Invalid event data format! Skipping corrupted packet.\n")
        
        # A tiny sleep interval simulates a streaming engine's micro-cycles
        time.sleep(1)

except KeyboardInterrupt:
    print("\n\n=== [STREAMING] Shutdown Signal Received. Pipeline Suspended. ===")