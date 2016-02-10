      googlepage = "https://script.google.com/macros/s/"
      mygooglekey = "AKfycbyDLLxRSLBLtjr_0wSsdgsdgsddggfqR6s21QtL9oJMhUqzFBs"
      wtime = time.strftime("%d/%m/%Y %H:%M:%S")
      content = urllib.urlopen("%s%s/exec?DATE=%s&Sensor1=%s&Sensor2=%s&Sensor3=%s&Sensor4=%s&Sensor5=%s&Sensor6=%s&Sensor7=%s&Sensor8=%s&Digital1=%s&Digital2=%s&Digital3=%s&Digital4=%s&Digital5=%s&Digital6=%s&Digital7=%s&Digital8=%s" %(googlepage, mygooglekey, wtime, sensor1_volts, sensor2_volts, sensor3_volts, sensor4_volts, sensor5_volts, sensor6_volts, sensor7_volts, sensor8_volts, digital1, digital2, digital3, digital4, digital5, digital6, digital7, digital8)).read()
