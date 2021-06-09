import json
import pytest
from starlette import responses
from starlette.responses import Response
from starlette.testclient import TestClient

def test_create_summary(test_app_with_db: TestClient):
    response = test_app_with_db.post("/summaries/", data=json.dumps({"url": "https://foo.bar"}))
    
    assert response.status_code == 201
    assert response.json()["url"] == "https://foo.bar"
    
def test_create_summaries_invalid_json(test_app: TestClient):
    response = test_app.post("/summaries/", data=json.dumps({}))
    
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }
    
def test_read_summary(test_app_with_db: TestClient):
    # save one
    response = test_app_with_db.post("/summaries/", data = json.dumps({"url": "https://foo.bar"}))
    summary_id = response.json()["id"]
    
    response = test_app_with_db.get(f"/summaries/{summary_id}/")
    assert response.status_code == 200
    
    response_dict = response.json()
    assert response_dict["id"] == summary_id
    assert response_dict["url"] == "https://foo.bar"
    assert response_dict["summary"]
    assert response_dict["created_at"]
    
def test_read_summary_incorrect_id(test_app_with_db:TestClient):
    # dont save anything
    response = test_app_with_db.get("/summaries/10000") # send an ID that does not exist
    
    assert response.status_code == 404
    assert response.json()["detail"] == "Summary not found"
    
def test_read_all_summaries(test_app_with_db: TestClient):
    # save one
    response = test_app_with_db.post("/summaries/", data = json.dumps({"url": "https://foo.bar"}))
    summary_id = response.json()["id"]
    
    response = test_app_with_db.get("/summaries/")
    assert response.status_code == 200
    
    response_list = response.json()
    
    assert len(list(filter(lambda x: x["id"] == summary_id, response_list))) == 1