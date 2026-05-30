from http import HTTPStatus
from http.client import HTTPException
from flask import Flask, render_template


def register_exception_handlers(server: Flask):

    @server.errorhandler(HTTPStatus.NOT_FOUND)
    def not_found_handler(error: HTTPException):
        return render_template("pages/404.html")
