X = 1
while X == 1:
	Volume = 0
	Accuracy = 0
	Aiming_time = 0
	Weight = 0
	Recoil = 0
	Durability = 0
	Sound = 0
	Firerate = 0

	print("""
 1 ACT Marksman Barrel: +Volume +Accuracy +Aiming time +Weight -Recoil
 2 ELF Tactical Barrel: -Volume -Accuracy -Aiming time +Weight -Recoil
 3 SMC Infantry Barrel: +Volume +Accuracy +Aiming time -Weight +Recoil
 4 LFL Killteam Barrel: -Volume --Accuracy -Aiming time -Weight +Recoil +Durability
 5 THI Special Forces Integrated Suppressor: -Sound ++Weight ++Aiming time ++Accuracy +Volume -Recoil
 6 THI Operative Integrated Suppressor: -Sound -Volume +Recoil \n """)

	Barrel = int(input("Select Barrel: "))

	if Barrel == 1:
		Volume = Volume + 1
		Accuracy = Accuracy + 1
		Aiming_time = Aiming_time + 1
		Weight = Weight + 1
		Recoil = Recoil - 1
	elif Barrel == 2:
		Volume = Volume - 1
		Accuracy = Accuracy - 1
		Aiming_time = Aiming_time - 1
		Weight = Weight + 1
		Recoil = Recoil - 1	
	elif Barrel == 3:
		Volume = Volume + 1
		Accuracy = Accuracy + 1
		Aiming_time = Aiming_time + 1
		Weight = Weight - 1
		Recoil = Recoil + 1	
	elif Barrel == 4:
		Volume = Volume - 1
		Accuracy = Accuracy - 2
		Aiming_time = Aiming_time - 1
		Weight = Weight - 1
		Recoil = Recoil + 1
		Durability = Durability + 1
	elif Barrel == 5:
		Aiming_time = Aiming_time + 2
		Weight = Weight + 2
		Sound = Sound - 1
		Accuracy = Accuracy + 2
		Volume = Volume + 1
		Recoil = Recoil - 1
	elif Barrel == 6:
		Sound = Sound - 1
		Volume = Volume - 1
		Recoil = Recoil + 1

	print("""
 1 ACT Spec Ops Handguard: ++Accuracy +Weight -Recoil +Volume +Aiming time
 2 LFL Trench Warfare Handguard: --Recoil +Weight -Volume -Aiming time -Accuracy
 3 THI Intervention Handguard: -Weight +Recoil -Volume -Aiming time
 4 LFL Firesupport Handguard: --Recoil +Weight +Volume +Aiming time +Accuracy
 5 SMC Trooper Handguard: -Weight +Volume +Aiming time +Accuracy
 6 ELF Tactical Handguard: +Weight -Recoil -Volume -Aiming time \n """)

	Handguard = int(input("Select Handguard: "))

	if Handguard == 1:
		Accuracy = Accuracy + 2
		Weight = Weight + 1
		Recoil = Recoil - 1
		Volume = Volume + 1
		Aiming_time = Aiming_time + 1
	elif Handguard == 2:
		Recoil = Recoil - 2
		Weight = Weight + 1
		Volume = Volume - 1
		Aiming_time = Aiming_time - 1
		Accuracy = Accuracy - 1
	elif Handguard == 3:
		Weight = Weight - 1
		Recoil = Recoil + 1
		Volume = Volume - 1
		Aiming_time = Aiming_time - 1
	elif Handguard == 4:
		Recoil = Recoil - 2
		Weight = Weight + 1
		Volume = Volume + 1
		Aiming_time = Aiming_time + 1
		Accuracy = Accuracy + 1
	elif Handguard == 5:
		Weight = Weight - 1
		Volume = Volume + 1
		Aiming_time = Aiming_time + 1
		Accuracy = Accuracy + 1
	elif Handguard == 6:
		Weight = Weight + 1
		Recoil = Recoil - 1
		Volume = Volume - 1
		Aiming_time = Aiming_time - 1

	print("""
 1 ACT Marksman Receiver Assembly: .308, Magazine-fed
 2 LFL Vanguard Receiver Assembly: .308, Belt-fed
 3 SMC Marine Receiver Assembly: .223, Magazine-fed
 4 LFL Bunkerbuster Receiver Assembly: .223, Belt-fed
 5 ACT Sniper Receiver Assembly: .50, Magazine-fed
 6 LFL Overwatch Reciever Assembly: .50, Belt-fed \n """)
		
	Receiver = int(input("Select Receiver: "))

	if Receiver == 1:
		Caliber = ".308"
		Loading = "Magazine-fed"
	elif Receiver == 2:
		Caliber = ".308"
		Loading = "Belt-fed"
	elif Receiver == 3:
		Caliber = ".223"
		Loading = "Magazine-fed"
	elif Receiver == 4:
		Caliber = ".223"
		Loading = "Belt-fed"
	elif Receiver == 5:
		Caliber = ".50"
		Loading = "Magazine-fed"
	elif Receiver == 6:
		Caliber = ".50"
		Loading = "Belt-fed"

	print("""
 1 ELF Studded Grip: -Aiming time -Accuracy
 2 THI Quick-Response Grip: -Aiming time +Recoil
 3 LFL Imprint Grip: -Accuracy -Recoil
 4 ACT Scout Grip: +Aiming time -Recoil \n """)

	Grip = int(input("Select Grip: "))

	if Grip == 1:
		Aiming_time = Aiming_time - 1
		Accuracy = Accuracy - 1
	elif Grip == 2:
		Aiming_time = Aiming_time - 1
		Recoil = Recoil + 1
	elif Grip == 3:
		Accuracy = Accuracy - 1
		Recoil = Recoil - 1
	elif Grip == 4:
		Aiming_time = Aiming_time + 1
		Recoil = Recoil - 1

	print("""
 1 LFL Hair Trigger Mechanism: +Firerate --Accuracy, Automatic
 2 THI Snapshot Trigger Mechanism: -Aiming time -Firerate +Accuracy, Semi-auto
 3 ACT Marksman Trigger Mechanism: -Firerate ++Accuracy, Semi-auto
 4 ELF Rapidfire Trigger Mechanism: +Firerate, Semi-auto
 5 ELF Twitch Trigger Mechanism: +Firerate -Accuracy, Burst-fire
 6 SMC Ranger Trigger Mechanism: -Aiming time -Firerate -Accuracy, Selective-burst
 7 ELF Firesupport Trigger Mechanism: --Firerate, Selective-auto
 8 THI Operations Trigger Mechanism: -Firerate, Selective-burst
 9 SMC Assault Trigger Mechanism: -Aiming time --Firerate -Accuracy, Selective-auto \n """)
	 
	Trigger = int(input("Select Trigger: "))

	if Trigger == 1:
		Firerate = Firerate + 1
		Accuracy = Accuracy - 2
		Firemode = ("Automatic")
	elif Trigger == 2:
		Aiming_time = Aiming_time - 1
		Firerate = Firerate - 1
		Accuracy = Accuracy + 1
		Firemode = ("Semi-auto")
	elif Trigger == 3:
		Firerate = Firerate - 1
		Accuracy = Accuracy + 2
		Firemode = ("Semi-auto")
	elif Trigger == 4:
		Firerate = Firerate + 1
		Firemode = ("Semi-auto")
	elif Trigger == 5:
		Firerate = Firerate + 1
		Accuracy = Accuracy - 1
		Firemode = ("Burst-fire")
	elif Trigger == 6:
		Aiming_time = Aiming_time - 1
		Firerate = Firerate - 1
		Accuracy = Accuracy - 1
		Firemode = ("Selective-burst")
	elif Trigger == 7:
		Firerate = Firerate - 2
		Firemode = ("Selective-auto")
	elif Trigger == 8:
		Firerate = Firerate - 1
		Firemode = ("Selective-burst")
	elif Trigger == 9:
		Aiming_time = Aiming_time - 1
		Firerate = Firerate - 2
		Accuracy = Accuracy - 1
		Firemode = ("Selective-auto")

	print("\n Volume: ", Volume, "\n Accuracy: ", Accuracy, "\n Aiming_time: ", Aiming_time, "\n Weight: ", Weight, "\n Recoil: ", Recoil, "\n Durability: ", Durability, "\n Sound: ", Sound, "\n Firerate: ", Firerate, "\n Caliber: ", Caliber, "\n Loading-mode: ", Loading, "\n Firemode: ", Firemode)
	X = int(input("try again? 1Y 0N "))
