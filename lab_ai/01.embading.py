import tensorflow  as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(3 , 5), # 3 * 5 둘이 곱한게 파라미터라는 수
                                    ])

model.summary()

'''
그래픽 카드의 모니터의 띄울 색상을 인공지능 -> GPGPU 색상 계산에만
쓰연던 것을 계산을 빠르게 해주는 것으로 활용. GPU 의 강력한 성능 이용
embeding model

행렬곱

'''

