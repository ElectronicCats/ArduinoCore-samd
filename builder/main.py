##########################################################################
#
#   Electronic Cats SAPI de CV 2020
#       http://www.electroniccats.com/
# 
##########################################################################

from os.path import join
from SCons.Script import (AlwaysBuild, Default, DefaultEnvironment)
from colorama import Fore

env = DefaultEnvironment()
print( Fore.GREEN + '<<<<<<<<<<<< ' + env.BoardConfig().get("name").upper() + " 2019 ElectronicCats >>>>>>>>>>>>" + Fore.BLACK )

elf = env.BuildProgram()
bin = env.CreateBin( join("$BUILD_DIR", "${PROGNAME}"), elf ) 
hex = env.CreateHex( join("$BUILD_DIR", "${PROGNAME}"), elf ) 
AlwaysBuild( hex, bin )

#env.Depends(hex, env.CreateBin( join("$BUILD_DIR", "${PROGNAME}"), elf ))

upload = env.Alias("upload", hex, [ env.VerboseAction("$UPLOADCMD", "\n"), env.VerboseAction("", "\n") ] )
AlwaysBuild( upload )    

Default( hex, bin )