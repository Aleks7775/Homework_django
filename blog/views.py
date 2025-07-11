from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog
from django.urls import reverse_lazy, reverse


class BlogListView(ListView):
    model = Blog
    fields = ['title', 'content']
    template_name = 'blogs/blog_list.html'

    def get_queryset(self):
        return Blog.objects.filter(publication_sign=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    template_name = "blogs/blog_form.html"
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blogs/blog_form.html"
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
   model = Blog
   template_name = "blogs/blog_confirm_delete.html"
   success_url = reverse_lazy('blog:blog_list')


