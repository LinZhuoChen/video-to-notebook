---
course_slug: diffusion-lm-vizuara
idx: 15
title: 'Lecture 14: Diffusion LLM Inference Pipeline'
video_url: https://www.youtube.com/watch?v=3dzjtDLaUJM
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.11
  end_sec: 51.91
  text: 'The last step which we need to do is the The last step which we need to do
    is the

    actual step of dnoising. actual step of dnoising. actual step of dnoising.

    What is dnoising? Well, dnoising is What is dnoising? Well, dnoising is What is
    dnoising? Well, dnoising is

    essentially starting from noise. essentially starting from noise. essentially
    starting from noise.

    Starting from complete noise like in the Starting from complete noise like in
    the Starting from complete noise like in the

    case of images, we start with noisy case of images, we start with noisy case of
    images, we start with noisy

    images and slowly our aim is to get to images and slowly our aim is to get to
    images and slowly our aim is to get to

    that probability distribution where the that probability distribution where the
    that probability distribution where the

    true image actually lives. If the true image actually lives. If the true image
    actually lives. If the

    training has been done correctly, then training has been done correctly, then
    training has been done correctly, then

    dn noising should actually help us to dn noising should actually help us to dn
    noising should actually help us to

    recover images in that exact or in the recover images in that exact or in the
    recover images in that exact or in the

    true probability distribution space or true probability distribution space or
    true probability distribution space or

    as close as possible to the true as close as possible to the true as close as
    possible to the true

    probability distribution space. What probability distribution space. What probability
    distribution space. What

    does it mean if training has been done does it mean if training has been done
    does it mean if training has been done

    correctly? Well, what it means is that correctly? Well, what it means is that
    correctly? Well, what it means is that

    if at each step of the training process, if at each step of the training process,
    if at each step of the training process,

    we are able to predict the noise which we are able to predict the noise which
    we are able to predict the noise which

    has been added. So at each step, has been added. So at each step, has been added.
    So at each step,

    yeah, at each step of the training'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 1
  start_sec: 51.91
  end_sec: 95.04
  text: 'yeah, at each step of the training yeah, at each step of the training

    process, if we are able to predict how process, if we are able to predict how
    process, if we are able to predict how

    much noise has been added in that step, much noise has been added in that step,
    much noise has been added in that step,

    essentially when we reverse when we essentially when we reverse when we essentially
    when we reverse when we

    reverse it or when we start from noise, reverse it or when we start from noise,
    reverse it or when we start from noise,

    we will be able to get back to the true we will be able to get back to the true
    we will be able to get back to the true

    image. That''s the whole idea. So if we image. That''s the whole idea. So if we
    image. That''s the whole idea. So if we

    at each step if we are able to predict at each step if we are able to predict
    at each step if we are able to predict

    how much noise is added to make a noisy how much noise is added to make a noisy
    how much noise is added to make a noisy

    image if we start from the noisy image image if we start from the noisy image
    image if we start from the noisy image

    we will be able to go back in the we will be able to go back in the we will be
    able to go back in the

    reverse direction. reverse direction. reverse direction.

    So in the case of images it''s fine right So in the case of images it''s fine
    right So in the case of images it''s fine right

    because in the case of images usually because in the case of images usually because
    in the case of images usually

    the dnoising might look something like the dnoising might look something like
    the dnoising might look something like

    this. Yeah like this we start from a this. Yeah like this we start from a this.
    Yeah like this we start from a

    completely noisy image and then we completely noisy image and then we completely
    noisy image and then we

    recover the clean image. So we start recover the clean image. So we start'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 2
  start_sec: 95.04
  end_sec: 135.44
  text: 'recover the clean image. So we start

    from a complete noisy image and then we from a complete noisy image and then we
    from a complete noisy image and then we

    recover Chinese characters as the recover Chinese characters as the recover Chinese
    characters as the

    dnoising proceeds. Right? But in the dnoising proceeds. Right? But in the dnoising
    proceeds. Right? But in the

    case of language, how does it happen? case of language, how does it happen? case
    of language, how does it happen?

    What does it mean by completely noisy What does it mean by completely noisy What
    does it mean by completely noisy

    image? We have already seen that a image? We have already seen that a image? We
    have already seen that a

    completely noisy or what does it mean by completely noisy or what does it mean
    by completely noisy or what does it mean by

    completely noisy text? It means that we completely noisy text? It means that we
    completely noisy text? It means that we

    start with a text in which everything is start with a text in which everything
    is start with a text in which everything is

    fully masked. So let''s say this is the fully masked. So let''s say this is the
    fully masked. So let''s say this is the

    text in which everything is fully text in which everything is fully text in which
    everything is fully

    masked. We have a beginning of sequence masked. We have a beginning of sequence
    masked. We have a beginning of sequence

    and an end of sequence. Let''s ignore and an end of sequence. Let''s ignore and
    an end of sequence. Let''s ignore

    that for a moment. But we have three that for a moment. But we have three that
    for a moment. But we have three

    masks over here. That''s how the dnoising masks over here. That''s how the dnoising
    masks over here. That''s how the dnoising

    process actually starts. What we have to process actually starts. What we have
    to process actually starts. What we have to

    do is that now the model is trained. The do is that now the model is trained.
    The do is that now the model is trained. The

    parameters of the model will not change parameters of the model will not change'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 3
  start_sec: 135.44
  end_sec: 182.159
  text: 'parameters of the model will not change

    in the dnoising process. The model is in the dnoising process. The model is in
    the dnoising process. The model is

    fully trained. Um so all these fully trained. Um so all these fully trained. Um
    so all these

    parameters which we have seen over here, parameters which we have seen over here,
    parameters which we have seen over here,

    those parameters will not change. Okay. those parameters will not change. Okay.
    those parameters will not change. Okay.

    What happens in the dnoising is that we What happens in the dnoising is that we
    What happens in the dnoising is that we

    have to slowly uncover these masks and have to slowly uncover these masks and
    have to slowly uncover these masks and

    predict what was there here in the first predict what was there here in the first
    predict what was there here in the first

    place. Okay. place. Okay. place. Okay.

    So let''s say we want to d noiseise from So let''s say we want to d noiseise from
    So let''s say we want to d noiseise from

    a fully noisy text which is this. The a fully noisy text which is this. The a
    fully noisy text which is this. The

    way the dnoising works in the case of way the dnoising works in the case of way
    the dnoising works in the case of

    language diffusion is through four language diffusion is through four language
    diffusion is through four

    steps. First, if we have in the forward steps. First, if we have in the forward
    steps. First, if we have in the forward

    pass, if we have time steps 1 2 3 4 or pass, if we have time steps 1 2 3 4 or
    pass, if we have time steps 1 2 3 4 or

    in this case, we had six time steps, in this case, we had six time steps, in this
    case, we had six time steps,

    right? In the forward pass, we had six right? In the forward pass, we had six
    right? In the forward pass, we had six

    time steps over here. If we had four time steps over here. If we had four time
    steps over here. If we had four

    time steps, for example, in the D time steps, for example, in the D'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 4
  start_sec: 182.159
  end_sec: 229.67
  text: 'time steps, for example, in the D

    noising process, we have to go backwards noising process, we have to go backwards
    noising process, we have to go backwards

    from four. So, we have to go 4 3 2 1, from four. So, we have to go 4 3 2 1, from
    four. So, we have to go 4 3 2 1,

    right? So, we have to start with four right? So, we have to start with four right?
    So, we have to start with four

    and then we have to sample the tokens and then we have to sample the tokens and
    then we have to sample the tokens

    for each of these masks. So we have to for each of these masks. So we have to
    for each of these masks. So we have to

    pass this sequence through the trained pass this sequence through the trained
    pass this sequence through the trained

    model and then see what the token model and then see what the token model and
    then see what the token

    prediction is at each of these masks prediction is at each of these masks prediction
    is at each of these masks

    at each of these positions. Then what we at each of these positions. Then what
    we at each of these positions. Then what we

    have to see is that which position is have to see is that which position is have
    to see is that which position is

    predicted most confidently predicted most confidently predicted most confidently

    and we have to uncover these masks and we have to uncover these masks and we have
    to uncover these masks

    sequentially. Right? So in the first sequentially. Right? So in the first sequentially.
    Right? So in the first

    iteration we only uncover one mask and iteration we only uncover one mask and
    iteration we only uncover one mask and

    keep all the other masks. keep all the other masks. keep all the other masks.

    Okay. Okay. Okay.

    Which mask is uncovered? the mass for Which mask is uncovered? the mass for Which
    mask is uncovered? the mass for

    which the prediction has the highest which the prediction has the highest which
    the prediction has the highest

    confidence of course. So let me let confidence of course. So let me let confidence
    of course. So let me let

    let''s take an example. Okay. So if this'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 5
  start_sec: 229.67
  end_sec: 282.16
  text: 'let''s take an example. Okay. So if this let''s take an example. Okay. So
    if this

    is the input sequence we start at time is the input sequence we start at time
    is the input sequence we start at time

    equal to 4. So we start in the reverse equal to 4. So we start in the reverse
    equal to 4. So we start in the reverse

    manner. We pass this input sequence manner. We pass this input sequence manner.
    We pass this input sequence

    through my entire architecture which is through my entire architecture which is
    through my entire architecture which is

    now trained. When I say my entire now trained. When I say my entire now trained.
    When I say my entire

    architecture, this input sequence passed architecture, this input sequence passed
    architecture, this input sequence passed

    through is passed through this whole through is passed through this whole through
    is passed through this whole

    architecture. architecture. architecture.

    So let me bring it over here. This input So let me bring it over here. This input
    So let me bring it over here. This input

    sequence is passed sequence is passed sequence is passed

    um this input sequence is passed through um this input sequence is passed through
    um this input sequence is passed through

    this whole architecture. this whole architecture. this whole architecture.

    And if I clean this up a bit be easier And if I clean this up a bit be easier
    And if I clean this up a bit be easier

    for you. Yeah, this input sequence is for you. Yeah, this input sequence is for
    you. Yeah, this input sequence is

    passed through this whole architecture. passed through this whole architecture.
    passed through this whole architecture.

    And here we don''t compute the loss And here we don''t compute the loss And here
    we don''t compute the loss

    because the training has already been because the training has already been because
    the training has already been

    done, right? But what we do compute here done, right? But what we do compute here
    done, right? But what we do compute here

    is what''s the predicted uh logits is what''s the predicted uh logits is what''s
    the predicted uh logits

    matrix? matrix? matrix?

    What is the predicted logits matrix? What is the predicted logits matrix?'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 6
  start_sec: 282.16
  end_sec: 358.15
  text: 'What is the predicted logits matrix?

    Um so let''s say we have position number Um so let''s say we have position number
    Um so let''s say we have position number

    we have three main positions which we have three main positions which we have
    three main positions which

    matter right because the beginning of matter right because the beginning of matter
    right because the beginning of

    sequence and end of sequence does not sequence and end of sequence does not sequence
    and end of sequence does not

    matter. We have position one position 2 matter. We have position one position
    2 matter. We have position one position 2

    and position three. So let''s say the and position three. So let''s say the and
    position three. So let''s say the

    logits matrix is something like this. logits matrix is something like this. logits
    matrix is something like this.

    The logit''s matrix for position one is The logit''s matrix for position one is
    The logit''s matrix for position one is

    122 06.22 06.22

    and 336. 0 0 let''s say and point 2 here. Uh for 0 0 let''s say and point 2 here.
    Uh for

    position three it is 0.1 let''s say same position three it is 0.1 let''s say same
    position three it is 0.1 let''s say same

    0 0. Now the way it works is that um 0 0. Now the way it works is that um 0 0.
    Now the way it works is that um

    let''s see now for position number one this is now for position number one this
    is

    position number one we see the maximum position number one we see the maximum
    position number one we see the maximum

    confidence is here and uh our dictionary confidence is here and uh our dictionary
    confidence is here and uh our dictionary

    actually is a actually is a actually is a

    uh our dictionary is uh our dictionary is uh our dictionary is

    let''s see what our dictionary is I think let''s see what our dictionary is I
    think let''s see what our dictionary is I think

    the dictionary is beginning of sequence the dictionary is beginning of sequence
    the dictionary is beginning of sequence

    end of sequence sequence mask end of sequence sequence mask end of sequence sequence
    mask

    then we have a b and c right so let''s'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 7
  start_sec: 358.15
  end_sec: 436.8
  text: 'then we have a b and c right so let''s then we have a b and c right so let''s

    actually actually actually

    take some different values of my let me take some different values of my let me
    take some different values of my let me

    refresh this what I want to do here is that I want to what I want to do here is
    that I want to

    take uh different um I want to take different values of my um I want to take different
    values of my

    now it''s working so let me rub this a now it''s working so let me rub this a
    now it''s working so let me rub this a

    bit bit bit

    okay okay okay

    and let''s say the values here are such and let''s say the values here are such
    and let''s say the values here are such

    that it''s 1 0 08 that it''s 1 0 08 that it''s 1 0 08

    and.1 and.1 and.1

    and this is also 0.100 08 and.1 okay so and this is also 0.100 08 and.1 okay so
    and this is also 0.100 08 and.1 okay so

    for this position for position number for this position for position number for
    this position for position number

    one the maximum confidence is for token one the maximum confidence is for token
    one the maximum confidence is for token

    C. So we''ll predict C with this C. So we''ll predict C with this C. So we''ll
    predict C with this

    confidence for position number. So let''s confidence for position number. So let''s
    confidence for position number. So let''s

    say this is.1 and8 and this is 1 and8. say this is.1 and8 and this is 1 and8.
    say this is.1 and8 and this is 1 and8.

    So for position two also it''s C and for So for position two also it''s C and
    for So for position two also it''s C and for

    position three also it''s C. position three also it''s C. position three also
    it''s C.

    Um so for position and actually the Um so for position and actually the Um so
    for position and actually the

    confidence let''s say it''s 336 here. So confidence let''s say it''s 336 here.
    So confidence let''s say it''s 336 here. So

    let''s let''s let''s

    change this again. change this again.'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 8
  start_sec: 436.8
  end_sec: 487.599
  text: 'change this again.

    Sorry for that. So let''s say this 336 Sorry for that. So let''s say this 336
    Sorry for that. So let''s say this 336

    and this 336. Let''s say everything is and this 336. Let''s say everything is
    and this 336. Let''s say everything is

    the same for all. So I''ll just uh the same for all. So I''ll just uh the same
    for all. So I''ll just uh

    take this and copy paste for all. take this and copy paste for all. take this
    and copy paste for all.

    Yeah. Yeah. So then I look at the token with Yeah. So then I look at the token
    with

    the maximum confidence and that''s C the maximum confidence and that''s C the
    maximum confidence and that''s C

    which is the last entry year for all my which is the last entry year for all my
    which is the last entry year for all my

    positions. Right. So after sampling my positions. Right. So after sampling my
    positions. Right. So after sampling my

    prediction should be CCC, right? But prediction should be CCC, right? But prediction
    should be CCC, right? But

    since we have just started the since we have just started the since we have just
    started the

    unmasking, unmasking, unmasking,

    we must end step three. So this first we must end step three. So this first we
    must end step three. So this first

    step we should end with three masks. step we should end with three masks. step
    we should end with three masks.

    That''s the rule. So when we start unmask That''s the rule. So when we start unmask
    That''s the rule. So when we start unmask

    unmasking, first we''ll end this step unmasking, first we''ll end this step unmasking,
    first we''ll end this step

    with three masks. Then we''ll have two with three masks. Then we''ll have two
    with three masks. Then we''ll have two

    masks. Then we''ll have one mask and then masks. Then we''ll have one mask and
    then masks. Then we''ll have one mask and then

    we''ll have no mask. That''s the idea. So we''ll have no mask. That''s the idea.
    So we''ll have no mask. That''s the idea. So

    we need three masks here. So again we''ll we need three masks here. So again we''ll'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 9
  start_sec: 487.599
  end_sec: 532.24
  text: 'we need three masks here. So again we''ll

    mask all these three. So these three mask all these three. So these three mask
    all these three. So these three

    stay in masks. That''s the output from stay in masks. That''s the output from
    stay in masks. That''s the output from

    the first dinoising step. Then we move the first dinoising step. Then we move
    the first dinoising step. Then we move

    to the second dinoising step which is to the second dinoising step which is to
    the second dinoising step which is

    time equal to three. Again let''s say time equal to three. Again let''s say time
    equal to three. Again let''s say

    position number one from the logits position number one from the logits position
    number one from the logits

    matrix we have that it samples A with matrix we have that it samples A with matrix
    we have that it samples A with

    maximum confidence. Position two we have maximum confidence. Position two we have
    maximum confidence. Position two we have

    sample C with maximum confidence and sample C with maximum confidence and sample
    C with maximum confidence and

    position three we have sample C with position three we have sample C with position
    three we have sample C with

    maximum confidence. So after sampling we maximum confidence. So after sampling
    we maximum confidence. So after sampling we

    should get beginning of sequence A C and should get beginning of sequence A C
    and should get beginning of sequence A C and

    end of sequence. Now after the second D end of sequence. Now after the second
    D end of sequence. Now after the second D

    noising step we need to keep two masks. noising step we need to keep two masks.
    noising step we need to keep two masks.

    So the whole idea is that so I''ll tell So the whole idea is that so I''ll tell
    So the whole idea is that so I''ll tell

    you here step step number four step you here step step number four step you here
    step step number four step

    three step two and step one at the end three step two and step one at the end
    three step two and step one at the end

    of this step we have to keep three masks of this step we have to keep three masks'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 10
  start_sec: 532.24
  end_sec: 571.99
  text: 'of this step we have to keep three masks

    at the end of this step we have to keep at the end of this step we have to keep
    at the end of this step we have to keep

    two masks at the end of this step which two masks at the end of this step which
    two masks at the end of this step which

    we have to keep one mask and at the end we have to keep one mask and at the end
    we have to keep one mask and at the end

    of the final step zero mask so that''s my of the final step zero mask so that''s
    my of the final step zero mask so that''s my

    final thing which will appear on the final thing which will appear on the final
    thing which will appear on the

    screen this is exactly what''s happening screen this is exactly what''s happening
    screen this is exactly what''s happening

    here we start with entire all masks and here we start with entire all masks and
    here we start with entire all masks and

    then we remove the masks one after one then we remove the masks one after one
    then we remove the masks one after one

    during the noising process I''m just during the noising process I''m just during
    the noising process I''m just

    showing you how what''s the logic to be showing you how what''s the logic to be
    showing you how what''s the logic to be

    followed for demasking. followed for demasking. followed for demasking.

    So now here we have step three right and So now here we have step three right
    and So now here we have step three right and

    I have a c and c but I have to keep two I have a c and c but I have to keep two
    I have a c and c but I have to keep two

    masks. So which are the two masks I will masks. So which are the two masks I will
    masks. So which are the two masks I will

    keep I will keep the two masks with the keep I will keep the two masks with the
    keep I will keep the two masks with the

    highest highest highest

    um um um

    or I will keep so which what what will I'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 11
  start_sec: 571.99
  end_sec: 609.44
  text: 'or I will keep so which what what will I or I will keep so which what what
    will I

    unmask? So I have to keep two masks here unmask? So I have to keep two masks here
    unmask? So I have to keep two masks here

    right? So I have to unmask one thing. right? So I have to unmask one thing. right?
    So I have to unmask one thing.

    What''s the thing I''ll unmask? I''ll What''s the thing I''ll unmask? I''ll What''s
    the thing I''ll unmask? I''ll

    unmask the thing with the highest unmask the thing with the highest unmask the
    thing with the highest

    confidence. Right? So either position confidence. Right? So either position confidence.
    Right? So either position

    two or three because position one has two or three because position one has two
    or three because position one has

    slightly lower confidence. So by default slightly lower confidence. So by default
    slightly lower confidence. So by default

    let''s say unmask this position which is let''s say unmask this position which
    is let''s say unmask this position which is

    position number two. I could have position number two. I could have position number
    two. I could have

    unmasked position three also but let''s unmasked position three also but let''s
    unmasked position three also but let''s

    say I unmask position two here. So then say I unmask position two here. So then
    say I unmask position two here. So then

    the input at the next step is Bos mask C the input at the next step is Bos mask
    C the input at the next step is Bos mask C

    mask and EOS. I pass it through the mask and EOS. I pass it through the mask and
    EOS. I pass it through the

    entire architecture. I get the logits entire architecture. I get the logits entire
    architecture. I get the logits

    and let''s say again I sample A C and A. and let''s say again I sample A C and
    A. and let''s say again I sample A C and A.

    At this position we have a probab At this position we have a probab At this position
    we have a probab

    confidence of 3175. At this we have a confidence of 3175. At this we have a'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 12
  start_sec: 609.44
  end_sec: 654.24
  text: 'confidence of 3175. At this we have a

    confidence of 336 and at this we have a confidence of 336 and at this we have
    a confidence of 336 and at this we have a

    confidence of 3175. Now here the rule is confidence of 3175. Now here the rule
    is confidence of 3175. Now here the rule is

    that we have to unmask we have to keep that we have to unmask we have to keep
    that we have to unmask we have to keep

    one mask. So we have to unmask two which one mask. So we have to unmask two which
    one mask. So we have to unmask two which

    are the two I will unmask. Again I''ll are the two I will unmask. Again I''ll
    are the two I will unmask. Again I''ll

    unmask those ones with the maximum unmask those ones with the maximum unmask those
    ones with the maximum

    confidence which are these two. confidence which are these two. confidence which
    are these two.

    Uh I could have unmasked this also but Uh I could have unmasked this also but
    Uh I could have unmasked this also but

    by default let''s say I unmasked this. So by default let''s say I unmasked this.
    So by default let''s say I unmasked this. So

    I unmask position one and I unmask I unmask position one and I unmask I unmask
    position one and I unmask

    position two. position two. position two.

    Then at the last step I have this input Then at the last step I have this input
    Then at the last step I have this input

    sequence B ac and only one mask and then sequence B ac and only one mask and then
    sequence B ac and only one mask and then

    I pass it through the input I pass it through the input I pass it through the
    input

    architecture. I get that the after architecture. I get that the after architecture.
    I get that the after

    sampling we have BOS ACC and EOS. sampling we have BOS ACC and EOS. sampling we
    have BOS ACC and EOS.

    Um and this is the logits matrix right. Um and this is the logits matrix right.
    Um and this is the logits matrix right.

    So at first position I sample A with So at first position I sample A with'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 13
  start_sec: 654.24
  end_sec: 705.509
  text: 'So at first position I sample A with

    confidence of 3175. At second position I confidence of 3175. At second position
    I confidence of 3175. At second position I

    sample C with confidence 336. At third sample C with confidence 336. At third
    sample C with confidence 336. At third

    position I sample C with confidence.336. So here I have to not keep any mask.
    So So here I have to not keep any mask. So

    I have to unmask everything. So the I have to unmask everything. So the I have
    to unmask everything. So the

    answer will now this everything will be answer will now this everything will be
    answer will now this everything will be

    unmasked. So the answer final answer unmasked. So the answer final answer unmasked.
    So the answer final answer

    final generated sequence is beginning of final generated sequence is beginning
    of final generated sequence is beginning of

    sequence A C C and end of sequence. sequence A C C and end of sequence. sequence
    A C C and end of sequence.

    That''s the sequence which is generated That''s the sequence which is generated
    That''s the sequence which is generated

    by the diffusion language model. Now by the diffusion language model. Now by the
    diffusion language model. Now

    that''s the end of it. We did the that''s the end of it. We did the that''s the
    end of it. We did the

    dnoising and that''s the generated dnoising and that''s the generated dnoising
    and that''s the generated

    sequence produced by the dnoising sequence produced by the dnoising sequence produced
    by the dnoising

    process. This is what it looks like in process. This is what it looks like in
    process. This is what it looks like in

    action. So here you see we start with action. So here you see we start with action.
    So here you see we start with

    all the masks. So if you give a prompt all the masks. So if you give a prompt
    all the masks. So if you give a prompt

    the prompt along with these masks along the prompt along with these masks along
    the prompt along with these masks along

    with all the masks are passed to the with all the masks are passed to the with
    all the masks are passed to the

    input architecture and wherever there is'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 14
  start_sec: 705.509
  end_sec: 752.88
  text: 'input architecture and wherever there is input architecture and wherever
    there is

    mask that slowly unmasked right. So here mask that slowly unmasked right. So here
    mask that slowly unmasked right. So here

    we have 128 steps. So right now I just we have 128 steps. So right now I just
    we have 128 steps. So right now I just

    showed you four steps for 128 steps we showed you four steps for 128 steps we
    showed you four steps for 128 steps we

    slowly unmask everything one after slowly unmask everything one after slowly unmask
    everything one after

    another. Right? So just see how fast the another. Right? So just see how fast
    the another. Right? So just see how fast the

    inference happens here compared to the inference happens here compared to the
    inference happens here compared to the

    next token prediction. Right. So let''s next token prediction. Right. So let''s
    next token prediction. Right. So let''s

    play this GIF if it opens. So see everything is masked right now. So see everything
    is masked right now.

    Right? Nothing is unmasked. We have 128 Right? Nothing is unmasked. We have 128
    Right? Nothing is unmasked. We have 128

    masks here. Now things are slowly masks here. Now things are slowly masks here.
    Now things are slowly

    getting unmasked here one after the getting unmasked here one after the getting
    unmasked here one after the

    other. Right? For some reason there is a other. Right? For some reason there is
    a other. Right? For some reason there is a

    weird black white contrast over here. So weird black white contrast over here.
    So weird black white contrast over here. So

    I can just bring this GIF over here and I can just bring this GIF over here and
    I can just bring this GIF over here and

    then just uh refresh it maybe. Yeah. See then just uh refresh it maybe. Yeah.
    See then just uh refresh it maybe. Yeah. See

    the masks are being removed one after the masks are being removed one after the
    masks are being removed one after

    the other. And uh it''s not auto the other. And uh it''s not auto the other. And
    uh it''s not auto

    reggressive which means it''s not one reggressive which means it''s not one'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 15
  start_sec: 752.88
  end_sec: 797.6
  text: 'reggressive which means it''s not one

    token at a time. Tokens masks can be token at a time. Tokens masks can be token
    at a time. Tokens masks can be

    unmasked here, masks can be unmasked at unmasked here, masks can be unmasked at
    unmasked here, masks can be unmasked at

    the top also. And everything happens the top also. And everything happens the
    top also. And everything happens

    very fast. That''s the advantage of very fast. That''s the advantage of very fast.
    That''s the advantage of

    diffusion models. Right? This is the diffusion models. Right? This is the diffusion
    models. Right? This is the

    generation process or this is the generation process or this is the generation
    process or this is the

    dnoising process. This dinoising process dnoising process. This dinoising process
    dnoising process. This dinoising process

    is again if you have done the noising is again if you have done the noising is
    again if you have done the noising

    process correctly which means if you process correctly which means if you process
    correctly which means if you

    have obtained a very low loss in the have obtained a very low loss in the have
    obtained a very low loss in the

    noising process dn noising is kind of noising process dn noising is kind of noising
    process dn noising is kind of

    guaranteed to work even in diffusion guaranteed to work even in diffusion guaranteed
    to work even in diffusion

    language models. So even theoretically language models. So even theoretically
    language models. So even theoretically

    this is a safe method but it just as this is a safe method but it just as this
    is a safe method but it just as

    we''ll see it takes a bit of time to we''ll see it takes a bit of time to we''ll
    see it takes a bit of time to

    train compared to train compared to train compared to

    auto reggressive language models. Okay, auto reggressive language models. Okay,
    auto reggressive language models. Okay,

    I hope all of you have understood the I hope all of you have understood the I
    hope all of you have understood the

    dnoising process, right? In dnoising, dnoising process, right? In dnoising, dnoising
    process, right? In dnoising,

    what happens is that let''s say you fully what happens is that let''s say you
    fully'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 16
  start_sec: 797.6
  end_sec: 846.71
  text: 'what happens is that let''s say you fully

    trained the model as we have seen trained the model as we have seen trained the
    model as we have seen

    before. Then you start with a sequence before. Then you start with a sequence
    before. Then you start with a sequence

    of masks. of masks. of masks.

    Let''s say if you want to predict a Let''s say if you want to predict a Let''s
    say if you want to predict a

    certain number of tokens, right? certain number of tokens, right? certain number
    of tokens, right?

    Uh you want to predict a certain number Uh you want to predict a certain number
    Uh you want to predict a certain number

    of tokens. All of them will be masked of tokens. All of them will be masked of
    tokens. All of them will be masked

    initially. initially. initially.

    Let''s say you want to predict 50 tokens. Let''s say you want to predict 50 tokens.
    Let''s say you want to predict 50 tokens.

    All of them will be masked. You pass All of them will be masked. You pass All
    of them will be masked. You pass

    those 50 tokens into the architecture those 50 tokens into the architecture those
    50 tokens into the architecture

    and you slowly go on unmasking the and you slowly go on unmasking the and you
    slowly go on unmasking the

    tokens one after the other. tokens one after the other. tokens one after the other.

    Uh that''s the whole idea of unmasking. Uh that''s the whole idea of unmasking.
    Uh that''s the whole idea of unmasking.

    It''s a very simple process but there is It''s a very simple process but there
    is It''s a very simple process but there is

    just one rule that uh you unmask those just one rule that uh you unmask those
    just one rule that uh you unmask those

    tokens which have the maximum confidence tokens which have the maximum confidence
    tokens which have the maximum confidence

    at every unmasking step. You unmask only at every unmasking step. You unmask only
    at every unmasking step. You unmask only

    those tokens which have maximum those tokens which have maximum those tokens which
    have maximum

    confidence and slowly you keep on confidence and slowly you keep on confidence
    and slowly you keep on

    unmasking one after the other. So this'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
- idx: 17
  start_sec: 846.71
  end_sec: 880.399
  text: 'unmasking one after the other. So this unmasking one after the other. So
    this

    video or this GIF which Andre Karpati video or this GIF which Andre Karpati video
    or this GIF which Andre Karpati

    shared. Now if you look at the right shared. Now if you look at the right shared.
    Now if you look at the right

    hand side the diffusion you should have hand side the diffusion you should have
    hand side the diffusion you should have

    a much better understanding. a much better understanding. a much better understanding.

    We start with masks and what is shown on We start with masks and what is shown
    on We start with masks and what is shown on

    the right hand side is just unmasking the right hand side is just unmasking the
    right hand side is just unmasking

    one step at a time. Whereas on the left hand side this is Whereas on the left
    hand side this is

    auto reggressive. It''s one token at a auto reggressive. It''s one token at a
    auto reggressive. It''s one token at a

    time. Whereas on the right hand side time. Whereas on the right hand side time.
    Whereas on the right hand side

    it''s masked get it''s masks getting it''s masked get it''s masks getting it''s
    masked get it''s masks getting

    unmasked one after the other. unmasked one after the other. unmasked one after
    the other.

    Okay. Now we''ll see a summary of the Okay. Now we''ll see a summary of the Okay.
    Now we''ll see a summary of the

    three characteristics of the diffusion three characteristics of the diffusion
    three characteristics of the diffusion

    language models.'
  concept_slugs:
  - diffusion-language-model
  - parallel-decoding
---
# Lecture 14: Diffusion LLM Inference Pipeline

See the structured chunks above.
