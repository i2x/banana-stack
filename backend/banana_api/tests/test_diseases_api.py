# banana_api/tests/test_diseases_api.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from model_bakery import baker

from banana_api.models import Disease


class DiseaseApiTests(APITestCase):
    def setUp(self):
        # สร้างตัวอย่างข้อมูล 25 records สำหรับทดสอบ pagination
        self.diseases = baker.make(Disease, _quantity=25)

    def test_list_diseases_default_pagination(self):
        """
        GET /api/diseases/ → 200
        ค่า default page=1, size=10
        response ต้องมี keys: count,total_pages,current_page,page_size,results
        """
        url = reverse('disease_list')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        body = res.json()

        for key in ["count", "total_pages", "current_page", "page_size", "results"]:
            self.assertIn(key, body)

        self.assertEqual(body["count"], 25)
        self.assertEqual(body["current_page"], 1)
        self.assertEqual(body["page_size"], 10)
        self.assertEqual(len(body["results"]), 10)

        # แต่ละ item ควรมี primary key ตามโมเดล: disease_id
        first_item = body["results"][0]
        self.assertIn("disease_id", first_item)
        for k in ["name", "description", "symptoms"]:
            self.assertIn(k, first_item)

    def test_list_diseases_custom_page_and_size(self):
        """
        GET /api/diseases/?page=2&size=7 → page 2 จะได้ 7 records
        """
        url = reverse('disease_list')
        res = self.client.get(url, {"page": 2, "size": 7})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        body = res.json()
        self.assertEqual(body["current_page"], 2)
        self.assertEqual(body["page_size"], 7)
        self.assertEqual(len(body["results"]), 7)
        self.assertIn("disease_id", body["results"][0])

    def test_list_diseases_invalid_query_params_return_400(self):
        """
        page/size ผิดรูปแบบ → 400 (ผ่าน custom exception handler)
        """
        url = reverse('disease_list')
        res = self.client.get(url, {"page": "abc", "size": "-5"})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_disease_detail_ok(self):
        """
        GET /api/diseases/<pk>/ → 200
        pk = disease_id
        """
        obj = self.diseases[0]
        url = reverse('disease_detail', args=[obj.pk])  # obj.pk == disease_id
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = res.json()

        self.assertIn("disease_id", data)
        self.assertEqual(data["disease_id"], obj.disease_id)
        for k in ["name", "description", "symptoms", "image_example"]:
            self.assertIn(k, data)

    def test_get_disease_detail_404(self):
        url = reverse('disease_detail', args=[999999])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
