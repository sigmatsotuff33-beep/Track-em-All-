import_relative "python_bridge"
import_relative "shodan_menu"

def main_menu
    puts "Ruby Track'em all"
    puts "Doc-Iota-Aegis  -- This project is easy so anyone can use it for more difficult projects check my git"
    puts "[1] run python cli directly"
    puts "[2] Shodan lookup "
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
        puts PythonBridge.call_python("image, path")
        when "4"
        ptint "Video path: "
        path = gets.chomp
        puts PythonBridge.call_python("video, path")
        when "0"
        puts "Exiting"
        exit
    else
        puts "Unknown option chose a good one bro its not hard cmon"
    end
end

loop {main_menu}
    