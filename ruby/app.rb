require_relative "python_bridge"
require_relative "shodan_menu"

def main_menu
  puts "Ruby Track'em all"
  puts "Doc-Iota-Aegis  -- v.OpenAlpha 0.2."
  puts "[1] run python cli directly"
  puts "[2] Shodan lookup"
  puts "[3] image analysis"
  puts "[4] video analysis"
  puts "0 exit"

  print "> "
  choice = gets.chomp

  case choice
  when "1"
    PythonBridge.run_python_cli

  when "2"
    ShodanMenu.prompt

  when "3"
    print "image path: "
    path = gets.chomp
    puts PythonBridge.call_python("image", path)

  when "4"
    print "video path: "
    path = gets.chomp
    puts PythonBridge.call_python("video", path)

  when "0"
    puts "Exiting"
    exit

  else
    puts "Unknown option — choose a proper one."
  end
end

loop { main_menu }
