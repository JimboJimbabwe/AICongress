import subprocess

counter = 0
counter_previous = 0  # Initialize counter_previous

while True:
    if counter < 1:
        print("Running scripts for counter < 1")
        
        # Run Initial State Backup
        subprocess.run(["python", "backup.py"])

        # Run congressStart.py
        subprocess.run(["python", "congressStart.py"])
        
        # Run sessionChoice.py
        subprocess.run(["python", "sessionChoice.py"])

        # Run VarEdit.py
        subprocess.run(["python", "VarEdit.py", "-default"])

        # Run start_hearing.py
        subprocess.run(["python", "start_hearing.py"])
        
        # Run collector.py
        subprocess.run(["python", "collector.py"])

        # Run cleaner.py
        subprocess.run(["python", "cleaner.py"])

        # Run cleaner.py
        subprocess.run(["python", "CustomUpload.py"])

        # When the scripts finish running, increment the counter
        counter += 1

    elif 0 < counter < 5:
        print(f"Doing the thing for 0 < counter < 5, current counter: {counter}")
        # Add your code for this condition here

        # Run start_hearing.py
        subprocess.run(["python", "start_hearing.py"])
        
        # Run collector.py
        subprocess.run(["python", "collector.py"])

        # Run cleaner.py
        subprocess.run(["python", "cleaner.py"])

        # Run cleaner.py
        subprocess.run(["python", "CustomUpload.py"])

        # When the thing ends, increment the counter
        counter += 1

    elif counter == 5:
        print("Doing the thing for counter == 5")
        # Add your code for this condition here

        # Run start_hearing.py
        subprocess.run(["python", "start_hearing.py"])
        
        # Run collector.py
        subprocess.run(["python", "collector.py"])

        # Run cleaner.py
        subprocess.run(["python", "cleaner.py"])

        # Run Meshed-RAG Memory Install
        subprocess.run(["python", "CustomUpload.py"])

        # Run Initial State Restore
        subprocess.run(["python", "assetClean.py"])

        # When the thing ends, reset the counter to 1
        counter = 1

    # Optionally, add a sleep or a break condition to prevent an infinite loop
    # For demonstration purposes, let's add a break after one full cycle
    if counter == 1 and counter_previous == 5:
        break
    counter_previous = counter
