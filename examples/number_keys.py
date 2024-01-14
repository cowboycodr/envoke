from envoke import envoke

# Create a macro sequence using number keys
sequence = envoke(start_delay=1)
sequence.key('3').key('2', interval=0.3).key('1')

# Add more number keys with optional random interval differences
sequence.key('3', interval=0.2, interval_diff=0.05).key('4', interval=0.4, interval_diff=0.1)

# Run the macro sequence
sequence.run(repeat=5)