---
course_slug: diffusion-lm-vizuara
idx: 4
title: 'Lecture 3: Generative AI through a probabilistic lens'
video_url: https://www.youtube.com/watch?v=V7YwRvac8wE
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.51
  end_sec: 49.039
  text: 'To really understand about how this To really understand about how this

    video links to image diffusion, I video links to image diffusion, I video links
    to image diffusion, I

    believe that we first need to understand believe that we first need to understand
    believe that we first need to understand

    a bit about how images are represented. a bit about how images are represented.
    a bit about how images are represented.

    Right? Right? Right?

    And there is some thing which is called And there is some thing which is called
    And there is some thing which is called

    as a pixel space which you can think of as a pixel space which you can think of
    as a pixel space which you can think of

    as a higher dimensional space. For the as a higher dimensional space. For the
    as a higher dimensional space. For the

    sake of simplicity, let''s say that we sake of simplicity, let''s say that we
    sake of simplicity, let''s say that we

    have Chinese symbols as image. So this have Chinese symbols as image. So this
    have Chinese symbols as image. So this

    is the first image. This is the second is the first image. This is the second
    is the first image. This is the second

    image. This is the third image. This is image. This is the third image. This is
    image. This is the third image. This is

    the fourth image etc. How do I represent the fourth image etc. How do I represent
    the fourth image etc. How do I represent

    this image in a higher dimensional this image in a higher dimensional this image
    in a higher dimensional

    space? space? space?

    If if I give you a vector, you can If if I give you a vector, you can If if I
    give you a vector, you can

    represent the vector in higher represent the vector in higher represent the vector
    in higher

    dimensions, right? If I give you dimensions, right? If I give you dimensions,
    right? If I give you

    something like 1,2 something like 1,2 something like 1,2

    you may say that this is one, this is you may say that this is one, this is you
    may say that this is one, this is

    two. So this is my vector. two. So this is my vector.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 1
  start_sec: 49.039
  end_sec: 91.28
  text: 'two. So this is my vector.

    That''s how you represent this vector. That''s how you represent this vector.
    That''s how you represent this vector.

    But how would you represent an entire But how would you represent an entire But
    how would you represent an entire

    image in a higher dimensional space? image in a higher dimensional space? image
    in a higher dimensional space?

    That''s where you come to the concept of That''s where you come to the concept
    of That''s where you come to the concept of

    something which is called as a pixel something which is called as a pixel something
    which is called as a pixel

    space. So to represent an image in a space. So to represent an image in a space.
    So to represent an image in a

    higher dimensional space, we first need higher dimensional space, we first need
    higher dimensional space, we first need

    to maybe convert this image into to maybe convert this image into to maybe convert
    this image into

    numbers. numbers. numbers.

    And the way to do that is to just break And the way to do that is to just break
    And the way to do that is to just break

    it down into pixels. So I''ve just zoomed it down into pixels. So I''ve just zoomed
    it down into pixels. So I''ve just zoomed

    into this image right now or one of the into this image right now or one of the
    into this image right now or one of the

    Chinese symbols. And you''ll see that Chinese symbols. And you''ll see that Chinese
    symbols. And you''ll see that

    when you zoom into an image, it''s just a when you zoom into an image, it''s just
    a when you zoom into an image, it''s just a

    grid of pixels. So then all I need to do grid of pixels. So then all I need to
    do grid of pixels. So then all I need to do

    is that let''s say I I take a look at all is that let''s say I I take a look at
    all is that let''s say I I take a look at all

    these pixels over here, right? And if these pixels over here, right? And if these
    pixels over here, right? And if

    this is 128x 128 pixels, I will arrange this is 128x 128 pixels, I will arrange'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 2
  start_sec: 91.28
  end_sec: 143.92
  text: 'this is 128x 128 pixels, I will arrange

    these 128x 128 pixels in a in a these 128x 128 pixels in a in a these 128x 128
    pixels in a in a

    u column. So imagine that you have this u column. So imagine that you have this
    u column. So imagine that you have this

    128x 128 pixels. You flatten it all out 128x 128 pixels. You flatten it all out
    128x 128 pixels. You flatten it all out

    and you stretch it into a big vector. and you stretch it into a big vector. and
    you stretch it into a big vector.

    That''s my vector now which represents That''s my vector now which represents
    That''s my vector now which represents

    this image. And this is a vector which this image. And this is a vector which
    this image. And this is a vector which

    has uh let me reduce the ink thickness a has uh let me reduce the ink thickness
    a has uh let me reduce the ink thickness a

    bit. This is a vector which has 16 384 bit. This is a vector which has 16 384
    bit. This is a vector which has 16 384

    dimensions. It''s a 16,000 dimensional dimensions. It''s a 16,000 dimensional
    dimensions. It''s a 16,000 dimensional

    vector and it will be represented in a vector and it will be represented in a
    vector and it will be represented in a

    16,000 dimensional space. So every image 16,000 dimensional space. So every image
    16,000 dimensional space. So every image

    lives in a higher dimensional vector lives in a higher dimensional vector lives
    in a higher dimensional vector

    space. space. space.

    Now how do you visualize this? Of Now how do you visualize this? Of Now how do
    you visualize this? Of

    course, we cannot visualize a 16,000 course, we cannot visualize a 16,000 course,
    we cannot visualize a 16,000

    dimensional space, but we can visualize dimensional space, but we can visualize
    dimensional space, but we can visualize

    two dimensional space, right? Uh so two dimensional space, right? Uh so two dimensional
    space, right? Uh so

    let''s say this is one image. It may live let''s say this is one image. It may
    live let''s say this is one image. It may live

    somewhere here in a pixel space. This is somewhere here in a pixel space. This
    is'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 3
  start_sec: 143.92
  end_sec: 197.28
  text: 'somewhere here in a pixel space. This is

    another image. It may live somewhere another image. It may live somewhere another
    image. It may live somewhere

    here in pixel space. So pixel space is here in pixel space. So pixel space is
    here in pixel space. So pixel space is

    essentially a domain of all the possible essentially a domain of all the possible
    essentially a domain of all the possible

    images, images, images,

    right? You take all the images, you right? You take all the images, you right?
    You take all the images, you

    break them down into 128x 128 pixels and break them down into 128x 128 pixels
    and break them down into 128x 128 pixels and

    then you put a dot corresponding to that then you put a dot corresponding to that
    then you put a dot corresponding to that

    image in your higher dimensional space. image in your higher dimensional space.
    image in your higher dimensional space.

    That''s your pixel space. And every image That''s your pixel space. And every
    image That''s your pixel space. And every image

    is mapped to a point. [snorts] Similar is mapped to a point. [snorts] Similar
    is mapped to a point. [snorts] Similar

    to if you''re living in a city, every to if you''re living in a city, every to
    if you''re living in a city, every

    person has a house in the city or every person has a house in the city or every
    person has a house in the city or every

    person stays in a building. Similarly, person stays in a building. Similarly,
    person stays in a building. Similarly,

    every image is mapped to a specific every image is mapped to a specific every
    image is mapped to a specific

    point in pixel space. Right? point in pixel space. Right? point in pixel space.
    Right?

    Now Now Now

    once you understand pixel space, there once you understand pixel space, there
    once you understand pixel space, there

    is also something which is called as the is also something which is called as
    the is also something which is called as the

    probability distribution of an image probability distribution of an image probability
    distribution of an image

    data set. Now this is something which data set. Now this is something which data
    set. Now this is something which

    you really need to understand. you really need to understand.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 4
  start_sec: 197.28
  end_sec: 243.12
  text: 'you really need to understand.

    How is the concept of probability How is the concept of probability How is the
    concept of probability

    distribution linked to that of an image distribution linked to that of an image
    distribution linked to that of an image

    data set. [snorts] data set. [snorts] data set. [snorts]

    Now while I''m explaining this course to Now while I''m explaining this course
    to Now while I''m explaining this course to

    you, I can directly explain this concept you, I can directly explain this concept
    you, I can directly explain this concept

    to you. But I also want to tell you a to you. But I also want to tell you a to
    you. But I also want to tell you a

    bit about how I learned right. So I have bit about how I learned right. So I have
    bit about how I learned right. So I have

    a notion of probability distribution. a notion of probability distribution. a
    notion of probability distribution.

    So if you take the pixel in one So if you take the pixel in one So if you take
    the pixel in one

    dimension, pixel in another dimension, dimension, pixel in another dimension,
    dimension, pixel in another dimension,

    you make a dot out of it. Right? you make a dot out of it. Right? you make a dot
    out of it. Right?

    Similarly, you sample from a huge number Similarly, you sample from a huge number
    Similarly, you sample from a huge number

    of images and you get a collection of of images and you get a collection of of
    images and you get a collection of

    these dots. you''ll get when you these dots. you''ll get when you these dots.
    you''ll get when you

    accumulate this you''ll get some surface accumulate this you''ll get some surface
    accumulate this you''ll get some surface

    or some sort of a contour that''s that or some sort of a contour that''s that
    or some sort of a contour that''s that

    can be visualized as the probability can be visualized as the probability can
    be visualized as the probability

    distribution of an email data set right distribution of an email data set right
    distribution of an email data set right

    and this is what I would have explained and this is what I would have explained'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 5
  start_sec: 243.12
  end_sec: 361.749
  text: 'and this is what I would have explained

    to you if chat GPT or Gemini did not to you if chat GPT or Gemini did not to you
    if chat GPT or Gemini did not

    exist but now let me actually take you exist but now let me actually take you
    exist but now let me actually take you

    through my process of if I really want through my process of if I really want
    through my process of if I really want

    to understand how probability to understand how probability to understand how
    probability

    distribution of an image is linked to distribution of an image is linked to distribution
    of an image is linked to

    pixel space let''s see how to use AI pixel space let''s see how to use AI pixel
    space let''s see how to use AI

    tools to understand this better. tools to understand this better. tools to understand
    this better.

    So, uh I''ll go to maybe Jiny So, uh I''ll go to maybe Jiny So, uh I''ll go to
    maybe Jiny

    [snorts] and let me say that hey Jiny [snorts] and let me say that hey Jiny [snorts]
    and let me say that hey Jiny

    I just understood the concept of I just understood the concept of I just understood
    the concept of

    pixel space. Essentially, Essentially,

    every image can be broken down into 128x every image can be broken down into 128x
    every image can be broken down into 128x

    128 [snorts] pixels 128 [snorts] pixels 128 [snorts] pixels

    flattened into a vector flattened into a vector flattened into a vector

    and uh mapped to a dot in 16384 dimensional space which is the pixel dimensional
    space which is the pixel

    space. Okay, let''s say I have images of Chinese let''s say I have images of Chinese

    symbols as my symbols as my symbols as my

    data set. data set. data set.

    I want to understand I want to understand I want to understand

    [snorts] [snorts] [snorts]

    the concept of probability probability

    distribution distribution distribution

    of an image data set. of an image data set. of an image data set.

    and how it''s linked and how it''s linked to the concept of and how it''s linked
    to the concept of

    pixel space. Can you explain this to me? Can you explain this to me?

    Let''s see. So the reason I''m showing'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 6
  start_sec: 361.749
  end_sec: 406.96
  text: 'Let''s see. So the reason I''m showing Let''s see. So the reason I''m showing

    this to you is because I want this this to you is because I want this this to
    you is because I want this

    learning material to be scalable for you learning material to be scalable for
    you learning material to be scalable for you

    when you are learning new new courses or when you are learning new new courses
    or when you are learning new new courses or

    new material because this is how I learn new material because this is how I learn
    new material because this is how I learn

    things in depth. I don''t get satisfied things in depth. I don''t get satisfied
    things in depth. I don''t get satisfied

    with things at a surface level or at an with things at a surface level or at an
    with things at a surface level or at an

    immediate level but I want to dive immediate level but I want to dive immediate
    level but I want to dive

    deeper. So let''s see. deeper. So let''s see. deeper. So let''s see.

    This is a fantastic question because it This is a fantastic question because it
    This is a fantastic question because it

    bridges the gap between linear algebra bridges the gap between linear algebra
    bridges the gap between linear algebra

    and the core logic of modern generative and the core logic of modern generative
    and the core logic of modern generative

    AI. AI. AI.

    Okay. Uh, first imagine that you are a Okay. Uh, first imagine that you are a
    Okay. Uh, first imagine that you are a

    god looking down at this 16,384 god looking down at this 16,384 god looking down
    at this 16,384

    dimensional space. If you were to close dimensional space. If you were to close
    dimensional space. If you were to close

    your eyes and throw a dart into this your eyes and throw a dart into this your
    eyes and throw a dart into this

    space, what would that image look like? space, what would that image look like?
    space, what would that image look like?

    It wouldn''t look like a Chinese symbol, It wouldn''t look like a Chinese symbol,
    It wouldn''t look like a Chinese symbol,

    right? It wouldn''t even look like a cat right? It wouldn''t even look like a
    cat'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 7
  start_sec: 406.96
  end_sec: 463.83
  text: 'right? It wouldn''t even look like a cat

    or a tree. It would look like random or a tree. It would look like random or a
    tree. It would look like random

    noise. So 99% of points in the pixel noise. So 99% of points in the pixel noise.
    So 99% of points in the pixel

    space are garbage noise. only a tiny space are garbage noise. only a tiny space
    are garbage noise. only a tiny

    tiny fraction of those points actually tiny fraction of those points actually
    tiny fraction of those points actually

    look like coherent Chinese symbols. look like coherent Chinese symbols. look like
    coherent Chinese symbols.

    Now imagine that you take your data set Now imagine that you take your data set
    Now imagine that you take your data set

    of 50,000 Chinese symbols and teleport of 50,000 Chinese symbols and teleport
    of 50,000 Chinese symbols and teleport

    them into this space at once. They won''t them into this space at once. They won''t
    them into this space at once. They won''t

    be scattered evenly. They will form a be scattered evenly. They will form a be
    scattered evenly. They will form a

    sheet or a cloud. This is the sheet or a cloud. This is the sheet or a cloud.
    This is the

    probability distribution. So imagine probability distribution. So imagine probability
    distribution. So imagine

    this for a moment, right? Imagine a huge this for a moment, right? Imagine a huge
    this for a moment, right? Imagine a huge

    space which is mostly empty and the space which is mostly empty and the space
    which is mostly empty and the

    Chinese symbols are living in a tiny Chinese symbols are living in a tiny Chinese
    symbols are living in a tiny

    section of that space. Maybe they are section of that space. Maybe they are section
    of that space. Maybe they are

    living in a shape which is looking like living in a shape which is looking like
    living in a shape which is looking like

    this. this. this.

    Maybe they are living in some different Maybe they are living in some different
    Maybe they are living in some different

    space. space.

    That''s called as a manifold. This is a space or this is a contour This is a space
    or this is a contour

    where all Chinese symbols are living.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 8
  start_sec: 463.83
  end_sec: 509.84
  text: 'where all Chinese symbols are living. where all Chinese symbols are living.

    That''s the probability distribution of That''s the probability distribution of
    That''s the probability distribution of

    this image data set. And it it''s a very this image data set. And it it''s a very
    this image data set. And it it''s a very

    small portion of a huge vast empty small portion of a huge vast empty small portion
    of a huge vast empty

    space. That''s what it means by a space. That''s what it means by a space. That''s
    what it means by a

    probability distribution of an image probability distribution of an image

    data set. You collect all the images data set. You collect all the images data
    set. You collect all the images

    from the data set. Let''s say 50,000 from the data set. Let''s say 50,000 from
    the data set. Let''s say 50,000

    images. You map them into pixel space images. You map them into pixel space images.
    You map them into pixel space

    and you see the shape which they are and you see the shape which they are and
    you see the shape which they are

    following. That is the probability following. That is the probability following.
    That is the probability

    distribution of that data set. If you distribution of that data set. If you distribution
    of that data set. If you

    were to imagine this is in two were to imagine this is in two were to imagine
    this is in two

    dimensions, maybe this is how the dimensions, maybe this is how the dimensions,
    maybe this is how the

    Chinese Chinese Chinese

    symbols probability distribution might symbols probability distribution might
    symbols probability distribution might

    look in two dimensions. So the rest of look in two dimensions. So the rest of
    look in two dimensions. So the rest of

    this space is not where the Chinese this space is not where the Chinese this space
    is not where the Chinese

    symbols are living because the symbols are living because the symbols are living
    because the

    probability of finding Chinese symbols probability of finding Chinese symbols
    probability of finding Chinese symbols

    is lower. is lower. is lower.

    A higher vertical magnitude indicates a A higher vertical magnitude indicates
    a A higher vertical magnitude indicates a

    higher probability of finding the higher probability of finding the'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 9
  start_sec: 509.84
  end_sec: 559.68
  text: 'higher probability of finding the

    Chinese symbol. Right? So now if you Chinese symbol. Right? So now if you Chinese
    symbol. Right? So now if you

    take a look at this 3D plot, right? If I take a look at this 3D plot, right? If
    I take a look at this 3D plot, right? If I

    go to this location, if I go to this go to this location, if I go to this go to
    this location, if I go to this

    location, this location and see the y location, this location and see the y location,
    this location and see the y

    the the the vertical magnitude is the the the the vertical magnitude is the the
    the the vertical magnitude is the

    highest over here. Right? So the highest over here. Right? So the highest over
    here. Right? So the

    probability of finding finding a Chinese probability of finding finding a Chinese
    probability of finding finding a Chinese

    symbol here is very high. Here it''s very symbol here is very high. Here it''s
    very symbol here is very high. Here it''s very

    high. In this manifold, it''s very high. high. In this manifold, it''s very high.
    high. In this manifold, it''s very high.

    But if I go outside this manifold, it''s But if I go outside this manifold, it''s
    But if I go outside this manifold, it''s

    essentially zero. Right? essentially zero. Right? essentially zero. Right?

    So this is a concept which all of you So this is a concept which all of you So
    this is a concept which all of you

    really really need to understand and really really need to understand and really
    really need to understand and

    master. This is called as probability master. This is called as probability master.
    This is called as probability

    distribution of images. This is the distribution of images. This is the distribution
    of images. This is the

    concept which many people don''t concept which many people don''t concept which
    many people don''t

    understand at all. They don''t understand understand at all. They don''t understand
    understand at all. They don''t understand

    how probability is linked to images. how probability is linked to images. how
    probability is linked to images.

    Basically, images are converted into Basically, images are converted into Basically,
    images are converted into

    pixels. Pixels are converted into flat pixels. Pixels are converted into flat'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 10
  start_sec: 559.68
  end_sec: 613.839
  text: 'pixels. Pixels are converted into flat

    vectors. Those are represented in higher vectors. Those are represented in higher
    vectors. Those are represented in higher

    dimensional space. dimensional space. dimensional space.

    You collect you take an image data set You collect you take an image data set
    You collect you take an image data set

    like let''s say Chinese symbols and you like let''s say Chinese symbols and you
    like let''s say Chinese symbols and you

    collect all these points together and collect all these points together and collect
    all these points together and

    see the manifold or shape which it see the manifold or shape which it see the
    manifold or shape which it

    forms. That''s the probability forms. That''s the probability forms. That''s the
    probability

    distribution. distribution. distribution.

    It''s a very small part of a huge empty It''s a very small part of a huge empty
    It''s a very small part of a huge empty

    space because rest is noise, space because rest is noise, space because rest is
    noise,

    right? And visualized in two dimensions, right? And visualized in two dimensions,
    right? And visualized in two dimensions,

    a probability distribution might look a probability distribution might look a
    probability distribution might look

    something like this. So points where the something like this. So points where
    the something like this. So points where the

    vertical magnitude is the highest, you vertical magnitude is the highest, you
    vertical magnitude is the highest, you

    are most likely to find the Chinese are most likely to find the Chinese are most
    likely to find the Chinese

    symbols. Okay, that''s the probability symbols. Okay, that''s the probability
    symbols. Okay, that''s the probability

    distribution of an image data set. distribution of an image data set. distribution
    of an image data set.

    Okay. And this is the main concept of Okay. And this is the main concept of Okay.
    And this is the main concept of

    generative AI or generative modeling. generative AI or generative modeling. generative
    AI or generative modeling.

    So one way to say that we are generating So one way to say that we are generating
    So one way to say that we are generating

    images through chat GPT is essentially images through chat GPT is essentially
    images through chat GPT is essentially

    saying that we are finding this this saying that we are finding this this'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 11
  start_sec: 613.839
  end_sec: 686.16
  text: 'saying that we are finding this this

    probability distribution. If you ask if probability distribution. If you ask if
    probability distribution. If you ask if

    you go to chat GPT right now or let''s you go to chat GPT right now or let''s
    you go to chat GPT right now or let''s

    say Google Gemini itself for that matter say Google Gemini itself for that matter
    say Google Gemini itself for that matter

    and I choose Nano Banana Pro and I say and I choose Nano Banana Pro and I say
    and I choose Nano Banana Pro and I say

    generate image of a Chinese symbol. generate image of a Chinese symbol. generate
    image of a Chinese symbol.

    What are we doing over here? We are What are we doing over here? We are What are
    we doing over here? We are

    sampling from the probability sampling from the probability sampling from the
    probability

    distribution of the Chinese symbols. distribution of the Chinese symbols. distribution
    of the Chinese symbols.

    Right? Right?

    So So So

    if you see over here, if you see over here, if you see over here,

    please pay very careful attention to please pay very careful attention to please
    pay very careful attention to

    this part because this will really this part because this will really this part
    because this will really

    motivate motivate motivate

    uh the concept of diffusion. Right? the concept of diffusion. Right?

    So when we say that the AI model generates when we say that the AI model generates

    a new image, a new image, a new image,

    what the AI model is actually doing over what the AI model is actually doing over
    what the AI model is actually doing over

    here is that it''s sampling from the here is that it''s sampling from the here
    is that it''s sampling from the

    probability distribution where the probability distribution where the probability
    distribution where the

    Chinese symbols live. So we are Chinese symbols live. So we are Chinese symbols
    live. So we are

    essentially finding the probability essentially finding the probability essentially
    finding the probability

    distribution of where the Chinese distribution of where the Chinese distribution
    of where the Chinese

    symbols are actually living. we are symbols are actually living. we are symbols
    are actually living. we are

    finding the true probability finding the true probability'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 12
  start_sec: 686.16
  end_sec: 745.59
  text: 'finding the true probability

    distribution or getting as close to it distribution or getting as close to it
    distribution or getting as close to it

    as possible. Right? So as possible. Right? So as possible. Right? So

    let''s look at generative AI from a let''s look at generative AI from a let''s
    look at generative AI from a

    completely different lens. Let''s say completely different lens. Let''s say completely
    different lens. Let''s say

    this is the probability distribution. this is the probability distribution. this
    is the probability distribution.

    Let''s say this is the probability Let''s say this is the probability Let''s say
    this is the probability

    distribution of a Chinese symbol data distribution of a Chinese symbol data distribution
    of a Chinese symbol data

    set. Right? set. Right? set. Right?

    What this actually means is that if we What this actually means is that if we
    What this actually means is that if we

    sample from this point, if we sample sample from this point, if we sample sample
    from this point, if we sample

    from this point, if we sample from this from this point, if we sample from this
    from this point, if we sample from this

    point, that will give us a high point, that will give us a high point, that will
    give us a high

    probability of finding a Chinese symbol. probability of finding a Chinese symbol.
    probability of finding a Chinese symbol.

    creating a generative model. creating a generative model. creating a generative
    model.

    What a generative AI model does in a What a generative AI model does in a What
    a generative AI model does in a

    probabilistic sense is that it tries and probabilistic sense is that it tries
    and probabilistic sense is that it tries and

    if you want the generative AI model to if you want the generative AI model to
    if you want the generative AI model to

    make Chinese symbols. What it actually doing is that it''s What it actually doing
    is that it''s

    trying to find a probability trying to find a probability trying to find a probability

    distribution which is as close as distribution which is as close as distribution
    which is as close as

    possible to the actual probability possible to the actual probability possible
    to the actual probability

    distribution. distribution.

    Right? So if I the red line is my true'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 13
  start_sec: 745.59
  end_sec: 802.069
  text: 'Right? So if I the red line is my true Right? So if I the red line is my
    true

    probability distribution probability distribution probability distribution

    and the purple line the purple line is and the purple line the purple line is
    and the purple line the purple line is

    my predicted probability distribution my predicted probability distribution my
    predicted probability distribution

    is my predicted probability is my predicted probability is my predicted probability

    distribution. One way or one lens to distribution. One way or one lens to distribution.
    One way or one lens to

    look at generative AI is that we are look at generative AI is that we are look
    at generative AI is that we are

    trying to find this purple line to be as trying to find this purple line to be
    as trying to find this purple line to be as

    close as possible to the red line. And close as possible to the red line. And
    close as possible to the red line. And

    let''s say we get that purple uh let''s say we get that purple uh let''s say we
    get that purple uh

    probability distribution. Then how do we probability distribution. Then how do
    we probability distribution. Then how do we

    generate images? This is the concept of generate images? This is the concept of
    generate images? This is the concept of

    sampling. sampling. sampling.

    To generate images, what we do is we To generate images, what we do is we To generate
    images, what we do is we

    sample from this predicted probability sample from this predicted probability
    sample from this predicted probability

    distribution. So if the predicted distribution. So if the predicted distribution.
    So if the predicted

    probability distribution looks like this probability distribution looks like this
    probability distribution looks like this

    and we have to sample from this and we have to sample from this and we have to
    sample from this

    probability distribution, naturally probability distribution, naturally probability
    distribution, naturally

    we''ll sample those points with higher we''ll sample those points with higher
    we''ll sample those points with higher

    probability, right? So then we''ll get probability, right? So then we''ll get
    probability, right? So then we''ll get

    this point. we''ll get this point which this point. we''ll get this point which
    this point. we''ll get this point which

    definitely do look like Chinese symbols'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 14
  start_sec: 802.069
  end_sec: 856.56
  text: 'definitely do look like Chinese symbols definitely do look like Chinese symbols

    because this purple probability because this purple probability because this purple
    probability

    distribution is close to the red distribution is close to the red distribution
    is close to the red

    probability distribution. probability distribution. probability distribution.

    So when you look at chat GPD and when So when you look at chat GPD and when So
    when you look at chat GPD and when

    you want to create an image let''s say you want to create an image let''s say
    you want to create an image let''s say

    create an image of a create an image of a create an image of a

    Chinese symbol. Currently what I''m teaching you is a Currently what I''m teaching
    you is a

    probabilistic viewpoint of generative probabilistic viewpoint of generative probabilistic
    viewpoint of generative

    AI. Right? When when I give this text, AI. Right? When when I give this text,
    AI. Right? When when I give this text,

    Chad GPT somehow understands that I have Chad GPT somehow understands that I have
    Chad GPT somehow understands that I have

    to find the probability distribution to find the probability distribution to find
    the probability distribution

    where Chinese symbols are living and try where Chinese symbols are living and
    try where Chinese symbols are living and try

    to match it to the actual probability to match it to the actual probability to
    match it to the actual probability

    distribution. Then it finds this purple distribution. Then it finds this purple
    distribution. Then it finds this purple

    probability distribution and then probability distribution and then probability
    distribution and then

    samples from it similar to what Gemini also did over similar to what Gemini also
    did over

    here. If you see we did create an image, here. If you see we did create an image,
    here. If you see we did create an image,

    right? I don''t know where it is right right? I don''t know where it is right
    right? I don''t know where it is right

    now, but we did create an image and your now, but we did create an image and your
    now, but we did create an image and your

    chat GPT. Yeah, this image Gemini chat GPT. Yeah, this image Gemini chat GPT.
    Yeah, this image Gemini

    sampled that purple probability sampled that purple probability'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 15
  start_sec: 856.56
  end_sec: 926.639
  text: 'sampled that purple probability

    distribution. distribution.

    Sampled from that purple probability Sampled from that purple probability Sampled
    from that purple probability

    distribution and created this image distribution and created this image distribution
    and created this image

    similar to what chat GPT is doing right similar to what chat GPT is doing right
    similar to what chat GPT is doing right

    now. It''s slowly getting to that now. It''s slowly getting to that now. It''s
    slowly getting to that

    probability distribution where Chinese probability distribution where Chinese
    probability distribution where Chinese

    symbols live and then sampling from it. symbols live and then sampling from it.
    symbols live and then sampling from it.

    This is the probabilistic lens. This is the probabilistic lens. This is the probabilistic
    lens.

    probabilistic lens lens

    of So usually when other people look at So usually when other people look at

    chat GPT they see that just an image is chat GPT they see that just an image is
    chat GPT they see that just an image is

    predicted right they don''t link it to predicted right they don''t link it to
    predicted right they don''t link it to

    probability but to truly understand probability but to truly understand probability
    but to truly understand

    diffusion this probabilistic lens is diffusion this probabilistic lens is diffusion
    this probabilistic lens is

    very very important right because what a very very important right because what
    a very very important right because what a

    diffusion model is actually doing is diffusion model is actually doing is diffusion
    model is actually doing is

    that that that

    it helps us to find the underlying it helps us to find the underlying it helps
    us to find the underlying

    probability distribution which means probability distribution which means probability
    distribution which means

    that it helps us to find this purple that it helps us to find this purple that
    it helps us to find this purple

    distribution to be as close as possible distribution to be as close as possible
    distribution to be as close as possible

    to the red distribution. So the purpose to the red distribution. So the purpose
    to the red distribution. So the purpose

    of a diffusion model is to find the of a diffusion model is to find the of a diffusion
    model is to find the

    underlying probability distribution. Let underlying probability distribution.
    Let'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 16
  start_sec: 926.639
  end_sec: 998.079
  text: 'underlying probability distribution. Let

    me write it here. Purpose Purpose of a diffusion model is to find Purpose of a
    diffusion model is to find

    the underlying probability distribution.

    That is the true purpose of a diffusion That is the true purpose of a diffusion
    That is the true purpose of a diffusion

    model. model. model.

    Now what we''ll see is how a diffusion Now what we''ll see is how a diffusion
    Now what we''ll see is how a diffusion

    model sets out to achieve this purpose. model sets out to achieve this purpose.
    model sets out to achieve this purpose.

    But one very careful thing which I But one very careful thing which I But one
    very careful thing which I

    already want you all to notice here is already want you all to notice here is
    already want you all to notice here is

    that there is nothing specific to images that there is nothing specific to images
    that there is nothing specific to images

    in this diffus in this definition. in this diffus in this definition. in this
    diffus in this definition.

    Right? If a purpose of a diffusion model Right? If a purpose of a diffusion model
    Right? If a purpose of a diffusion model

    is to find the underlying probability is to find the underlying probability is
    to find the underlying probability

    distribution, why can''t this same distribution, why can''t this same distribution,
    why can''t this same

    purpose be applied to text as well as purpose be applied to text as well as purpose
    be applied to text as well as

    images? Keep this in mind. However, now images? Keep this in mind. However, now
    images? Keep this in mind. However, now

    we are going to see how a diffusion we are going to see how a diffusion we are
    going to see how a diffusion

    model sets out to achieve this purpose. model sets out to achieve this purpose.

    So let''s look at the overall process of So let''s look at the overall process
    of So let''s look at the overall process of

    noising and denoising and how do we noising and denoising and how do we noising
    and denoising and how do we

    actually recover this underlying actually recover this underlying actually recover
    this underlying

    probability distribution.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
---
# Lecture 3: Generative AI through a probabilistic lens

See the structured chunks above.
