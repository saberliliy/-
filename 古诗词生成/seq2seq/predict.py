from keras.models import Model
from keras.layers import Input, LSTM, Dense
from keras import callbacks
import numpy as np
from keras.models import load_model

model_path = './s2s_2.h5'
model = load_model(model_path)
encoder_model = Model(encoder_inputs, encoder_state)

decoder_state_input_h = Input(shape=(latent_dim,))
decoder_state_input_c = Input(shape=(latent_dim,))
decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]

# 得到解码器的输出以及中间状态
decoder_outputs, state_h, state_c = decoder_lstm(decoder_inputs, initial_state=decoder_states_inputs)
decoder_states = [state_h, state_c]
decoder_outputs = decoder_dense(decoder_outputs)

decoder_model = Model([decoder_inputs] + decoder_states_inputs, [decoder_outputs]+decoder_states)

reverse_input_char_index = dict([(i, char) for char, i in input_token_index.items()])
reverse_target_char_index = dict([(i, char) for char, i in target_token_index.items()])



def decode_sequence(input_seq):
    # 将输入序列进行编码
    states_value = encoder_model.predict(input_seq)

    # 生成一个size=1的空序列
    target_seq = np.zeros((1, 1, num_decoder_tokens))
    # 将这个空序列的内容设置为开始字符
    target_seq[0, 0, target_token_index['\t']] = 1.

    # 进行字符恢复
    # 简单起见，假设batch_size = 1
    stop_condition = False
    decoded_sentence = ''

    while not stop_condition:
        output_tokens, h, c = decoder_model.predict([target_seq] + states_value)

        # sample a token
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = reverse_target_char_index[sampled_token_index]
        decoded_sentence += sampled_char

        # 退出条件：生成 \n 或者 超过最大序列长度
        if sampled_char == '\n' or len(decoded_sentence) > max_decoder_seq_length :
            stop_condition = True

        # 更新target_seq
        target_seq = np.zeros((1, 1, num_decoder_tokens))
        target_seq[0, 0, sampled_token_index] = 1.

        # 更新中间状态
        states_value = [h, c]

    return decoded_sentence



# 检验成果的时候到了,从训练集中选取一些句子做测试
# 效果还行（废话，从训练集里挑的数据）
for seq_index in range(1000, 1100):
    # batch_size = 1
    input_seq = encoder_input_data[seq_index:seq_index+1]
    decoded_sentence = decode_sequence(input_seq)

    print('-')
    print('Input sentence:', input_texts[seq_index])
    print('Decoded sentence:', decoded_sentence)
