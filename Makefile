.PHONY: backend frontend dev

backend:
	cd backend && uvicorn app:app --reload

frontend:
	cd frontend && npm run dev

dev:
	@echo "Start backend and frontend in separate terminals."