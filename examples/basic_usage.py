from envoke import envoke

# Create a macro sequence
sequence = envoke(start_delay=2)
sequence.enter(interval=0.5).key('a', interval=0.1)

# Run the macro
sequence.run()
