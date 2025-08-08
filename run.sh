#!/bin/bash

# Colors
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting AI Secure Voice Assistant...${NC}"

# Step 1: Start Backend (FastAPI)
echo -e "${GREEN}Launching Backend...${NC}"
cd backend
uvicorn app:app --reload &
BACKEND_PID=$!
cd ..

# Step 2: Start Frontend (Vue)
echo -e "${GREEN}Launching Frontend...${NC}"
cd frontend
npm install
npm run dev &
FRONTEND_PID=$!
cd ..

# Wait and trap CTRL+C
trap "echo -e '\nStopping...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT

echo -e "${GREEN}System running.${NC}"
wait
