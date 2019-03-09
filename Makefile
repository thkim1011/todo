SRC_DIR = src
INCLUDE_DIR = include
BUILD_DIR = build
BIN_DIR = bin

all: $(BUILD_DIR)/main.o $(BUILD_DIR)/entry.o $(BUILD_DIR)/date.o
	g++ $(BUILD_DIR)/main.o $(BUILD_DIR)/entry.o $(BUILD_DIR)/date.o -o $(BIN_DIR)/a.out


# main.cpp
$(BUILD_DIR)/main.o: $(SRC_DIR)/main.cpp
	g++ -I $(INCLUDE_DIR) -c $(SRC_DIR)/main.cpp -o $(BUILD_DIR)/main.o

# entry.cpp
$(BUILD_DIR)/entry.o: $(SRC_DIR)/entry.cpp
	g++ -I $(INCLUDE_DIR) -c $(SRC_DIR)/entry.cpp -o $(BUILD_DIR)/entry.o

# date.cpp
$(BUILD_DIR)/date.o: $(SRC_DIR)/date.cpp
	g++ -I $(INCLUDE_DIR) -c $(SRC_DIR)/date.cpp -o $(BUILD_DIR)/date.o
