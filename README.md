# Brightness-manager for X
File brightness.py:

  Variables:
  
    - steps - 
      Number of brightness levels

    - min_val -
      Minimal value for brightness

    - max_val -
      Maximum value for brightness
      
    - def_path -
      Path to directory with all these scripts
      
    !! VALUES ARE MULTIPLIED BY 10 !!
  
  Functions:
  
    - add() -
      Increases brightness by one level
    
    - sub() -
      Decreases brightness by one level
      
    - notify-send(msg) -
      Sends notification with custom message(msg)
    
    - read_val() -
      Reads current informations about screen brightness
      
    - set_brightness -
      Simple set brightness for X
      
    - save() -
      Saves current states to file

How to use:
  Firstly configure brightness.py for your own needs.
  Then, execute add.py or sub.py to manipulate screen brightness.
  I recommend bind these scripts to keyboard shortcuts.
  If you wanna reconfigure brightness.py just execute reset_bright.py to avoid unexpected problems and then, go edit main file.
