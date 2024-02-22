BASE_URL="http://localhost:6400"

curl -X POST "$BASE_URL"'/api/v1/todos/' \
	-H "Content-Type: application/json"\
	-d '{"title": "An example todo", "description": "this is an example todo"}'\
	--verbose
