from datetime import timedelta
from passlib.context import CryptContext
from pydantic import SecretStr
from flask_jwt_extended import create_access_token
from model.models import User
import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# ==================== #
#     JWT 配置         #
# ==================== #
ACCESS_TOKEN_EXPIRE_MINUTES: int = timedelta(hours=2)  # Token有效期默认2小时

# 密码哈希配置
PWD_HASH_ALGORITHM: str = "bcrypt"  # 密码哈希算法

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against a hash
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):  #加密算法
    """
    Hash a password
    """
    return pwd_context.hash(password)

def create_token(username) -> str:
    """
    Create a JWT access token
    """
    identity=username

    encoded_jwt= create_access_token(identity=identity,expires_delta=ACCESS_TOKEN_EXPIRE_MINUTES)
    return encoded_jwt  #返回token令牌