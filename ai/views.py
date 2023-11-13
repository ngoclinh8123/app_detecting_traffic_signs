from django.http import JsonResponse
import base64
import cv2
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from services.detecting_traffic_signs import detecting
import os
from tensorflow.keras.models import load_model


def index(request):
    return render(request, "index.html")


@csrf_exempt
def detect_traffic_sign(request):
    if request.method == "POST":
        # Nhận dữ liệu hình ảnh từ trình duyệt
        data = request.POST.get("image_data")

        img_data = base64.b64decode(data.split(",")[1])
        nparr = np.frombuffer(img_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Lưu trữ hình ảnh tạm thời
        temp_image_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "temp_image.jpg"
        )
        cv2.imwrite(temp_image_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

        # Trả về kết quả nhận diện cho trình duyệt
        result_json = detecting(temp_image_path)
        return JsonResponse(result_json)

    return HttpResponse("Invalid request method")
