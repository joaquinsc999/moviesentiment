from flask import jsonify

def json_response(data, status_code=200):
    if (data.get("message", 0) == 0):
        data["message"] = "Solicitud exitosa"
    if (data.get("status", 0) == 0):
        data["status"] = "success"
    return jsonify(data), status_code
