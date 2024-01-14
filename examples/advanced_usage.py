from envoke import envoke

# Advanced macro sequence with continuous run and random intervals
sequence = envoke()
sequence.keys(['left', 'right'], interval=0.2, interval_diff=0.05).space(interval=0.5)

# Run the macro continuously
sequence.run(start_delay=1, continuous=True)