def build_unet(n_classes=7, img_height=256, img-width=256, img_channels=3):

    inputs = Input((img_height, img-width, img_channels)
 

    #Encoder

    #block1
    convolution_1 = Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(inputs)
    convolution_2 = Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(convolution_1)
    pooling_1 = MaxPooling2D((2, 2))(convolution_2)

    #block2
    convolution_3 = Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(pooling_1)
    convolution_4 = Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(convolution_3)
    pooling_2 = MaxPooling2D((2, 2))(convolution_4)

    #block3
    convolution_5 = Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(pooling_2)
    concolution_6 = Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(convolution_5)
    pooling_3 = MaxPooling2D((2, 2))(concolution_6)

    
    #block4
    convolution_7 = Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(pooling_3)
    convolution_8 = Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(convolution_7)
    pooling_4 = MaxPooling2D(pool_size=(2, 2))(convolution_8 )

    
    #block5
    convolution_9 = Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(pooling_4)
    convolution_10 = Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(convolution_9)


    # Decoder branch

    #block6
    up_convolution_11 = Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(convolution_10)
    copy_crop_1 = concatenate([up_convolution_11, convolution_8])
    convolution_12 = Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u6)
    convolution_13 = Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c6)


    #block7
    up_convolution_14 = Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(c6)
    ucopy_crop_2 = concatenate([up_convolution_14, convolution_6])
    concolution_15 = Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u7)
    convolution_16 = Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c7)


    #block8
    up_convolution_17 = Conv2DTranspose(32, (2, 2), strides=(2, 2), padding='same')(c7)
    copy_crop3 = concatenate([up_convolution_17, convolution_4])
    convolution_18 = Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u8)
    convolution_19 = Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c8)


    #block9
    up_convolution_20 = Conv2DTranspose(16, (2, 2), strides=(2, 2), padding='same')(c8)
    copy_crop_4 = concatenate([up_convolution_20, convolution_2], axis=3)
    convolution_21 = Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u9)
    convolution_22 = Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c9)

    output_layer_23 = Conv2D(7, (1, 1), activation='softmax')(c9)

    model = Model(inputs=[inputs], outputs=[outputs])

    #NOTE: Compile the model in the main program to make it easy to test with various loss functions
    #model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    #model.summary()

    return model
