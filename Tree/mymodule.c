#include <Python.h>

// C 함수: 두 정수를 더함
static PyObject* my_add(PyObject* self, PyObject* args) {
    int a, b;
    // 파이썬에서 넘어온 인자를 C 변수로 변환
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    return PyLong_FromLong(a + b);  // 결과를 파이썬 int로 반환
}

// 모듈에 포함될 함수 목록
static PyMethodDef MyMethods[] = {
    {"add", my_add, METH_VARARGS, "Add two integers"},
    {NULL, NULL, 0, NULL}  // 종료 표시
};

// 모듈 정의
static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "mymodule",   // 모듈 이름
    "A simple C extension module", // 모듈 설명
    -1,
    MyMethods
};

// 모듈 초기화 함수
PyMODINIT_FUNC PyInit_mymodule(void) {
    return PyModule_Create(&mymodule);
}
