---
course_slug: diffusion-lm-vizuara
idx: 2
title: 'Lecture 1: Introduction to Diffusion Language Models'
video_url: https://www.youtube.com/watch?v=RqT8j_Bj8SA
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.669
  end_sec: 61.11
  text: 'Hello everyone. This is Dr. Raj Dandeek Hello everyone. This is Dr. Raj Dandeek

    and uh today I''m very excited to present and uh today I''m very excited to present
    and uh today I''m very excited to present

    this learning material to all of you. this learning material to all of you. this
    learning material to all of you.

    I''ve been thinking about this for quite I''ve been thinking about this for quite
    I''ve been thinking about this for quite

    some time now and uh some time now and uh some time now and uh

    just like many other things. Um when I just like many other things. Um when I
    just like many other things. Um when I

    started thinking about diffusion started thinking about diffusion started thinking
    about diffusion

    language models, I thought it was very language models, I thought it was very
    language models, I thought it was very

    difficult and uh the initial phase took difficult and uh the initial phase took
    difficult and uh the initial phase took

    a very long amount of time or a large a very long amount of time or a large a
    very long amount of time or a large

    amount of time for me to really amount of time for me to really amount of time
    for me to really

    understand what''s going on. But uh the understand what''s going on. But uh the
    understand what''s going on. But uh the

    final implementation final implementation final implementation

    and uh building it fully from scratch, and uh building it fully from scratch,
    and uh building it fully from scratch,

    comparing it with auto reggressive comparing it with auto reggressive comparing
    it with auto reggressive

    models was fairly straightforward and models was fairly straightforward and models
    was fairly straightforward and

    simple. simple. simple.

    So I could just show you that fast thing So I could just show you that fast thing
    So I could just show you that fast thing

    which I did towards the end where when which I did towards the end where when
    which I did towards the end where when

    things became clearer to me how I things became clearer to me how I things became
    clearer to me how I

    implemented language based diffusion implemented language based diffusion implemented
    language based diffusion

    models from scratch. But that''s not how'
  concept_slugs:
  - autoregressive-vs-diffusion
  - diffusion-language-model
- idx: 1
  start_sec: 61.11
  end_sec: 109.429
  text: 'models from scratch. But that''s not how models from scratch. But that''s
    not how

    I want this course or this learning I want this course or this learning I want
    this course or this learning

    material to be. I want you to take I material to be. I want you to take I material
    to be. I want you to take I

    want to take you all through the journey want to take you all through the journey
    want to take you all through the journey

    which I went through because the initial which I went through because the initial
    which I went through because the initial

    uh uh uh

    learning was difficult for me. Diffusion learning was difficult for me. Diffusion
    learning was difficult for me. Diffusion

    is not that simple. It''s not that is not that simple. It''s not that is not that
    simple. It''s not that

    straightforward. So to understand straightforward. So to understand straightforward.
    So to understand

    diffusion and to get to that stage where diffusion and to get to that stage where
    diffusion and to get to that stage where

    I could build a diffusion based language I could build a diffusion based language
    I could build a diffusion based language

    model from scratch was not easy. So this model from scratch was not easy. So this
    model from scratch was not easy. So this

    is not going to be like those is not going to be like those is not going to be
    like those

    traditional courses or learning traditional courses or learning traditional courses
    or learning

    materials where we directly start from materials where we directly start from
    materials where we directly start from

    the the the

    uh fundamentals directly start from the uh fundamentals directly start from the
    uh fundamentals directly start from the

    content basically. But I''m I''ll take you content basically. But I''m I''ll take
    you content basically. But I''m I''ll take you

    through a journey. I''ll take you through through a journey. I''ll take you through
    through a journey. I''ll take you through

    my story of how I stumbled upon my story of how I stumbled upon my story of how
    I stumbled upon

    diffusion models, how I was initially diffusion models, how I was initially diffusion
    models, how I was initially

    scared of them, then how I learned the'
  concept_slugs:
  - autoregressive-vs-diffusion
  - diffusion-language-model
- idx: 2
  start_sec: 109.429
  end_sec: 147.92
  text: 'scared of them, then how I learned the scared of them, then how I learned
    the

    subject, how I mastered the subject now subject, how I mastered the subject now
    subject, how I mastered the subject now

    so that you can follow along this so that you can follow along this so that you
    can follow along this

    journey with me. That''s my intention journey with me. That''s my intention journey
    with me. That''s my intention

    with this uh um course or learning with this uh um course or learning with this
    uh um course or learning

    material. I want to I want this to be a material. I want to I want this to be
    a material. I want to I want this to be a

    journey for all of you so that you feel journey for all of you so that you feel
    journey for all of you so that you feel

    relatable, right? Because whenever we relatable, right? Because whenever we relatable,
    right? Because whenever we

    start learning a new subject, it''s not start learning a new subject, it''s not
    start learning a new subject, it''s not

    easy. So I felt that if I documented my easy. So I felt that if I documented my
    easy. So I felt that if I documented my

    learning process or journey all of you learning process or journey all of you
    learning process or journey all of you

    will feel that okay you are also in a will feel that okay you are also in a will
    feel that okay you are also in a

    similar boat and this will give you more similar boat and this will give you more
    similar boat and this will give you more

    confidence to learn new subjects on your confidence to learn new subjects on your
    confidence to learn new subjects on your

    own. That being said at the end of this own. That being said at the end of this
    own. That being said at the end of this

    journey you will build a language model journey you will build a language model
    journey you will build a language model

    uh a diffusion based small language uh a diffusion based small language uh a diffusion
    based small language

    model fully from scratch. You''ll compare model fully from scratch. You''ll compare'
  concept_slugs:
  - autoregressive-vs-diffusion
  - diffusion-language-model
- idx: 3
  start_sec: 147.92
  end_sec: 186.239
  text: 'model fully from scratch. You''ll compare

    it with the auto reggressive language it with the auto reggressive language it
    with the auto reggressive language

    models. So it''s an amazing exercise or models. So it''s an amazing exercise or
    models. So it''s an amazing exercise or

    it''ll be a beautiful conclusion for all it''ll be a beautiful conclusion for
    all it''ll be a beautiful conclusion for all

    of you. As with all of the videos which of you. As with all of the videos which
    of you. As with all of the videos which

    we record at Vijara, this is going to be we record at Vijara, this is going to
    be we record at Vijara, this is going to be

    long form content. Uh these are not this long form content. Uh these are not this
    long form content. Uh these are not this

    is not a short content. I''ll explain is not a short content. I''ll explain is
    not a short content. I''ll explain

    everything in depth. Everything from everything in depth. Everything from everything
    in depth. Everything from

    scratch and from first principles. If scratch and from first principles. If scratch
    and from first principles. If

    you already know some aspect of what I''m you already know some aspect of what
    I''m you already know some aspect of what I''m

    about to explain. Uh you can skip that about to explain. Uh you can skip that
    about to explain. Uh you can skip that

    particular portion and move to the next particular portion and move to the next
    particular portion and move to the next

    part. But for a complete understanding, part. But for a complete understanding,
    part. But for a complete understanding,

    I recommend you to watch it all. Thanks I recommend you to watch it all. Thanks
    I recommend you to watch it all. Thanks

    again everyone and let''s get started.'
  concept_slugs:
  - autoregressive-vs-diffusion
  - diffusion-language-model
---
# Lecture 1: Introduction to Diffusion Language Models

See the structured chunks above.
