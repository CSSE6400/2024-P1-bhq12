BASE_URL="http://localhost:6400"

curl -X PUT "$BASE_URL"'/api/v1/todos/1' \
	-H "Content-Type: application/json"\
	-d '{"title": "An updated title"}'\
	--verbose
