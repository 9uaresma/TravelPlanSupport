OBJ		:= main.o
BIN 	:= main.exe
CPP		:= $(wildcard ../src/*.cpp)
INC		:= $(wildcard ../include/*.cpp)

SRCDIR		:= src
OBJDIR		:= obj
BINDIR		:= bin

# Default Make
all: directories $(BIN)

# ディレクトリ生成
directories:
	if not exist "$(BINDIR)" mkdir $(BINDIR)
	if not exist "$(OBJDIR)" mkdir $(OBJDIR)

# コンパイル
$(BIN):	$(CPP) $(INC)

	g++  $(CPP) $(INC) -o $(OBJDIR)/$(OBJ)
	g++ $(CPP) $(INC) -o $(BINDIR)/$(BIN)

clean:
	del /Q /S $(OBJDIR)
	del /Q /S $(BINDIR)




