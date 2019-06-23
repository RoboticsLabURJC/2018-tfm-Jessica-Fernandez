// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: tensorflow/core/debug/debug_service.proto
// Original file comments:
// Copyright 2016 The TensorFlow Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// ==============================================================================
//
#ifndef GRPC_tensorflow_2fcore_2fdebug_2fdebug_5fservice_2eproto__INCLUDED
#define GRPC_tensorflow_2fcore_2fdebug_2fdebug_5fservice_2eproto__INCLUDED

#include "tensorflow/core/debug/debug_service.pb.h"

#include <grpcpp/impl/codegen/async_stream.h>
#include <grpcpp/impl/codegen/async_unary_call.h>
#include <grpcpp/impl/codegen/method_handler_impl.h>
#include <grpcpp/impl/codegen/proto_utils.h>
#include <grpcpp/impl/codegen/rpc_method.h>
#include <grpcpp/impl/codegen/service_type.h>
#include <grpcpp/impl/codegen/status.h>
#include <grpcpp/impl/codegen/stub_options.h>
#include <grpcpp/impl/codegen/sync_stream.h>

namespace grpc {
class CompletionQueue;
class Channel;
class ServerCompletionQueue;
class ServerContext;
}  // namespace grpc

namespace tensorflow {

// EventListener: Receives Event protos, e.g., from debugged TensorFlow
// runtime(s).
class EventListener final {
 public:
  static constexpr char const* service_full_name() {
    return "tensorflow.EventListener";
  }
  class StubInterface {
   public:
    virtual ~StubInterface() {}
    // Client(s) can use this RPC method to send the EventListener Event protos.
    // The Event protos can hold information such as:
    //   1) intermediate tensors from a debugged graph being executed, which can
    //      be sent from DebugIdentity ops configured with grpc URLs.
    //   2) GraphDefs of partition graphs, which can be sent from special debug
    //      ops that get executed immediately after the beginning of the graph
    //      execution.
    std::unique_ptr< ::grpc::ClientReaderWriterInterface< ::tensorflow::Event, ::tensorflow::EventReply>> SendEvents(::grpc::ClientContext* context) {
      return std::unique_ptr< ::grpc::ClientReaderWriterInterface< ::tensorflow::Event, ::tensorflow::EventReply>>(SendEventsRaw(context));
    }
    std::unique_ptr< ::grpc::ClientAsyncReaderWriterInterface< ::tensorflow::Event, ::tensorflow::EventReply>> AsyncSendEvents(::grpc::ClientContext* context, ::grpc::CompletionQueue* cq, void* tag) {
      return std::unique_ptr< ::grpc::ClientAsyncReaderWriterInterface< ::tensorflow::Event, ::tensorflow::EventReply>>(AsyncSendEventsRaw(context, cq, tag));
    }
    std::unique_ptr< ::grpc::ClientAsyncReaderWriterInterface< ::tensorflow::Event, ::tensorflow::EventReply>> PrepareAsyncSendEvents(::grpc::ClientContext* context, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncReaderWriterInterface< ::tensorflow::Event, ::tensorflow::EventReply>>(PrepareAsyncSendEventsRaw(context, cq));
    }
    // Send the tracebacks of a TensorFlow execution call.
    virtual ::grpc::Status SendTracebacks(::grpc::ClientContext* context, const ::tensorflow::CallTraceback& request, ::tensorflow::EventReply* response) = 0;
    std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::tensorflow::EventReply>> AsyncSendTracebacks(::grpc::ClientContext* context, const ::tensorflow::CallTraceback& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::tensorflow::EventReply>>(AsyncSendTracebacksRaw(context, request, cq));
    }
    std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::tensorflow::EventReply>> PrepareAsyncSendTracebacks(::grpc::ClientContext* context, const ::tensorflow::CallTraceback& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::tensorflow::EventReply>>(PrepareAsyncSendTracebacksRaw(context, request, cq));
    }
    // Send a collection of source code files being debugged.
    virtual ::grpc::Status SendSourceFiles(::grpc::ClientContext* context, const ::tensorflow::DebuggedSourceFiles& request, ::tensorflow::EventReply* response) = 0;
    std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::tensorflow::EventReply>> AsyncSendSourceFiles(::grpc::ClientContext* context, const ::tensorflow::DebuggedSourceFiles& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::tensorflow::EventReply>>(AsyncSendSourceFilesRaw(context, request, cq));
    }
    std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::tensorflow::EventReply>> PrepareAsyncSendSourceFiles(::grpc::ClientContext* context, const ::tensorflow::DebuggedSourceFiles& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::tensorflow::EventReply>>(PrepareAsyncSendSourceFilesRaw(context, request, cq));
    }
  private:
    virtual ::grpc::ClientReaderWriterInterface< ::tensorflow::Event, ::tensorflow::EventReply>* SendEventsRaw(::grpc::ClientContext* context) = 0;
    virtual ::grpc::ClientAsyncReaderWriterInterface< ::tensorflow::Event, ::tensorflow::EventReply>* AsyncSendEventsRaw(::grpc::ClientContext* context, ::grpc::CompletionQueue* cq, void* tag) = 0;
    virtual ::grpc::ClientAsyncReaderWriterInterface< ::tensorflow::Event, ::tensorflow::EventReply>* PrepareAsyncSendEventsRaw(::grpc::ClientContext* context, ::grpc::CompletionQueue* cq) = 0;
    virtual ::grpc::ClientAsyncResponseReaderInterface< ::tensorflow::EventReply>* AsyncSendTracebacksRaw(::grpc::ClientContext* context, const ::tensorflow::CallTraceback& request, ::grpc::CompletionQueue* cq) = 0;
    virtual ::grpc::ClientAsyncResponseReaderInterface< ::tensorflow::EventReply>* PrepareAsyncSendTracebacksRaw(::grpc::ClientContext* context, const ::tensorflow::CallTraceback& request, ::grpc::CompletionQueue* cq) = 0;
    virtual ::grpc::ClientAsyncResponseReaderInterface< ::tensorflow::EventReply>* AsyncSendSourceFilesRaw(::grpc::ClientContext* context, const ::tensorflow::DebuggedSourceFiles& request, ::grpc::CompletionQueue* cq) = 0;
    virtual ::grpc::ClientAsyncResponseReaderInterface< ::tensorflow::EventReply>* PrepareAsyncSendSourceFilesRaw(::grpc::ClientContext* context, const ::tensorflow::DebuggedSourceFiles& request, ::grpc::CompletionQueue* cq) = 0;
  };
  class Stub final : public StubInterface {
   public:
    Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel);
    std::unique_ptr< ::grpc::ClientReaderWriter< ::tensorflow::Event, ::tensorflow::EventReply>> SendEvents(::grpc::ClientContext* context) {
      return std::unique_ptr< ::grpc::ClientReaderWriter< ::tensorflow::Event, ::tensorflow::EventReply>>(SendEventsRaw(context));
    }
    std::unique_ptr<  ::grpc::ClientAsyncReaderWriter< ::tensorflow::Event, ::tensorflow::EventReply>> AsyncSendEvents(::grpc::ClientContext* context, ::grpc::CompletionQueue* cq, void* tag) {
      return std::unique_ptr< ::grpc::ClientAsyncReaderWriter< ::tensorflow::Event, ::tensorflow::EventReply>>(AsyncSendEventsRaw(context, cq, tag));
    }
    std::unique_ptr<  ::grpc::ClientAsyncReaderWriter< ::tensorflow::Event, ::tensorflow::EventReply>> PrepareAsyncSendEvents(::grpc::ClientContext* context, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncReaderWriter< ::tensorflow::Event, ::tensorflow::EventReply>>(PrepareAsyncSendEventsRaw(context, cq));
    }
    ::grpc::Status SendTracebacks(::grpc::ClientContext* context, const ::tensorflow::CallTraceback& request, ::tensorflow::EventReply* response) override;
    std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::tensorflow::EventReply>> AsyncSendTracebacks(::grpc::ClientContext* context, const ::tensorflow::CallTraceback& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::tensorflow::EventReply>>(AsyncSendTracebacksRaw(context, request, cq));
    }
    std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::tensorflow::EventReply>> PrepareAsyncSendTracebacks(::grpc::ClientContext* context, const ::tensorflow::CallTraceback& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::tensorflow::EventReply>>(PrepareAsyncSendTracebacksRaw(context, request, cq));
    }
    ::grpc::Status SendSourceFiles(::grpc::ClientContext* context, const ::tensorflow::DebuggedSourceFiles& request, ::tensorflow::EventReply* response) override;
    std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::tensorflow::EventReply>> AsyncSendSourceFiles(::grpc::ClientContext* context, const ::tensorflow::DebuggedSourceFiles& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::tensorflow::EventReply>>(AsyncSendSourceFilesRaw(context, request, cq));
    }
    std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::tensorflow::EventReply>> PrepareAsyncSendSourceFiles(::grpc::ClientContext* context, const ::tensorflow::DebuggedSourceFiles& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::tensorflow::EventReply>>(PrepareAsyncSendSourceFilesRaw(context, request, cq));
    }

   private:
    std::shared_ptr< ::grpc::ChannelInterface> channel_;
    ::grpc::ClientReaderWriter< ::tensorflow::Event, ::tensorflow::EventReply>* SendEventsRaw(::grpc::ClientContext* context) override;
    ::grpc::ClientAsyncReaderWriter< ::tensorflow::Event, ::tensorflow::EventReply>* AsyncSendEventsRaw(::grpc::ClientContext* context, ::grpc::CompletionQueue* cq, void* tag) override;
    ::grpc::ClientAsyncReaderWriter< ::tensorflow::Event, ::tensorflow::EventReply>* PrepareAsyncSendEventsRaw(::grpc::ClientContext* context, ::grpc::CompletionQueue* cq) override;
    ::grpc::ClientAsyncResponseReader< ::tensorflow::EventReply>* AsyncSendTracebacksRaw(::grpc::ClientContext* context, const ::tensorflow::CallTraceback& request, ::grpc::CompletionQueue* cq) override;
    ::grpc::ClientAsyncResponseReader< ::tensorflow::EventReply>* PrepareAsyncSendTracebacksRaw(::grpc::ClientContext* context, const ::tensorflow::CallTraceback& request, ::grpc::CompletionQueue* cq) override;
    ::grpc::ClientAsyncResponseReader< ::tensorflow::EventReply>* AsyncSendSourceFilesRaw(::grpc::ClientContext* context, const ::tensorflow::DebuggedSourceFiles& request, ::grpc::CompletionQueue* cq) override;
    ::grpc::ClientAsyncResponseReader< ::tensorflow::EventReply>* PrepareAsyncSendSourceFilesRaw(::grpc::ClientContext* context, const ::tensorflow::DebuggedSourceFiles& request, ::grpc::CompletionQueue* cq) override;
    const ::grpc::internal::RpcMethod rpcmethod_SendEvents_;
    const ::grpc::internal::RpcMethod rpcmethod_SendTracebacks_;
    const ::grpc::internal::RpcMethod rpcmethod_SendSourceFiles_;
  };
  static std::unique_ptr<Stub> NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options = ::grpc::StubOptions());

  class Service : public ::grpc::Service {
   public:
    Service();
    virtual ~Service();
    // Client(s) can use this RPC method to send the EventListener Event protos.
    // The Event protos can hold information such as:
    //   1) intermediate tensors from a debugged graph being executed, which can
    //      be sent from DebugIdentity ops configured with grpc URLs.
    //   2) GraphDefs of partition graphs, which can be sent from special debug
    //      ops that get executed immediately after the beginning of the graph
    //      execution.
    virtual ::grpc::Status SendEvents(::grpc::ServerContext* context, ::grpc::ServerReaderWriter< ::tensorflow::EventReply, ::tensorflow::Event>* stream);
    // Send the tracebacks of a TensorFlow execution call.
    virtual ::grpc::Status SendTracebacks(::grpc::ServerContext* context, const ::tensorflow::CallTraceback* request, ::tensorflow::EventReply* response);
    // Send a collection of source code files being debugged.
    virtual ::grpc::Status SendSourceFiles(::grpc::ServerContext* context, const ::tensorflow::DebuggedSourceFiles* request, ::tensorflow::EventReply* response);
  };
  template <class BaseClass>
  class WithAsyncMethod_SendEvents : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service *service) {}
   public:
    WithAsyncMethod_SendEvents() {
      ::grpc::Service::MarkMethodAsync(0);
    }
    ~WithAsyncMethod_SendEvents() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status SendEvents(::grpc::ServerContext* context, ::grpc::ServerReaderWriter< ::tensorflow::EventReply, ::tensorflow::Event>* stream) final override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    void RequestSendEvents(::grpc::ServerContext* context, ::grpc::ServerAsyncReaderWriter< ::tensorflow::EventReply, ::tensorflow::Event>* stream, ::grpc::CompletionQueue* new_call_cq, ::grpc::ServerCompletionQueue* notification_cq, void *tag) {
      ::grpc::Service::RequestAsyncBidiStreaming(0, context, stream, new_call_cq, notification_cq, tag);
    }
  };
  template <class BaseClass>
  class WithAsyncMethod_SendTracebacks : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service *service) {}
   public:
    WithAsyncMethod_SendTracebacks() {
      ::grpc::Service::MarkMethodAsync(1);
    }
    ~WithAsyncMethod_SendTracebacks() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status SendTracebacks(::grpc::ServerContext* context, const ::tensorflow::CallTraceback* request, ::tensorflow::EventReply* response) final override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    void RequestSendTracebacks(::grpc::ServerContext* context, ::tensorflow::CallTraceback* request, ::grpc::ServerAsyncResponseWriter< ::tensorflow::EventReply>* response, ::grpc::CompletionQueue* new_call_cq, ::grpc::ServerCompletionQueue* notification_cq, void *tag) {
      ::grpc::Service::RequestAsyncUnary(1, context, request, response, new_call_cq, notification_cq, tag);
    }
  };
  template <class BaseClass>
  class WithAsyncMethod_SendSourceFiles : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service *service) {}
   public:
    WithAsyncMethod_SendSourceFiles() {
      ::grpc::Service::MarkMethodAsync(2);
    }
    ~WithAsyncMethod_SendSourceFiles() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status SendSourceFiles(::grpc::ServerContext* context, const ::tensorflow::DebuggedSourceFiles* request, ::tensorflow::EventReply* response) final override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    void RequestSendSourceFiles(::grpc::ServerContext* context, ::tensorflow::DebuggedSourceFiles* request, ::grpc::ServerAsyncResponseWriter< ::tensorflow::EventReply>* response, ::grpc::CompletionQueue* new_call_cq, ::grpc::ServerCompletionQueue* notification_cq, void *tag) {
      ::grpc::Service::RequestAsyncUnary(2, context, request, response, new_call_cq, notification_cq, tag);
    }
  };
  typedef WithAsyncMethod_SendEvents<WithAsyncMethod_SendTracebacks<WithAsyncMethod_SendSourceFiles<Service > > > AsyncService;
  template <class BaseClass>
  class WithGenericMethod_SendEvents : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service *service) {}
   public:
    WithGenericMethod_SendEvents() {
      ::grpc::Service::MarkMethodGeneric(0);
    }
    ~WithGenericMethod_SendEvents() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status SendEvents(::grpc::ServerContext* context, ::grpc::ServerReaderWriter< ::tensorflow::EventReply, ::tensorflow::Event>* stream) final override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
  };
  template <class BaseClass>
  class WithGenericMethod_SendTracebacks : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service *service) {}
   public:
    WithGenericMethod_SendTracebacks() {
      ::grpc::Service::MarkMethodGeneric(1);
    }
    ~WithGenericMethod_SendTracebacks() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status SendTracebacks(::grpc::ServerContext* context, const ::tensorflow::CallTraceback* request, ::tensorflow::EventReply* response) final override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
  };
  template <class BaseClass>
  class WithGenericMethod_SendSourceFiles : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service *service) {}
   public:
    WithGenericMethod_SendSourceFiles() {
      ::grpc::Service::MarkMethodGeneric(2);
    }
    ~WithGenericMethod_SendSourceFiles() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status SendSourceFiles(::grpc::ServerContext* context, const ::tensorflow::DebuggedSourceFiles* request, ::tensorflow::EventReply* response) final override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
  };
  template <class BaseClass>
  class WithStreamedUnaryMethod_SendTracebacks : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service *service) {}
   public:
    WithStreamedUnaryMethod_SendTracebacks() {
      ::grpc::Service::MarkMethodStreamed(1,
        new ::grpc::internal::StreamedUnaryHandler< ::tensorflow::CallTraceback, ::tensorflow::EventReply>(std::bind(&WithStreamedUnaryMethod_SendTracebacks<BaseClass>::StreamedSendTracebacks, this, std::placeholders::_1, std::placeholders::_2)));
    }
    ~WithStreamedUnaryMethod_SendTracebacks() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable regular version of this method
    ::grpc::Status SendTracebacks(::grpc::ServerContext* context, const ::tensorflow::CallTraceback* request, ::tensorflow::EventReply* response) final override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    // replace default version of method with streamed unary
    virtual ::grpc::Status StreamedSendTracebacks(::grpc::ServerContext* context, ::grpc::ServerUnaryStreamer< ::tensorflow::CallTraceback,::tensorflow::EventReply>* server_unary_streamer) = 0;
  };
  template <class BaseClass>
  class WithStreamedUnaryMethod_SendSourceFiles : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service *service) {}
   public:
    WithStreamedUnaryMethod_SendSourceFiles() {
      ::grpc::Service::MarkMethodStreamed(2,
        new ::grpc::internal::StreamedUnaryHandler< ::tensorflow::DebuggedSourceFiles, ::tensorflow::EventReply>(std::bind(&WithStreamedUnaryMethod_SendSourceFiles<BaseClass>::StreamedSendSourceFiles, this, std::placeholders::_1, std::placeholders::_2)));
    }
    ~WithStreamedUnaryMethod_SendSourceFiles() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable regular version of this method
    ::grpc::Status SendSourceFiles(::grpc::ServerContext* context, const ::tensorflow::DebuggedSourceFiles* request, ::tensorflow::EventReply* response) final override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    // replace default version of method with streamed unary
    virtual ::grpc::Status StreamedSendSourceFiles(::grpc::ServerContext* context, ::grpc::ServerUnaryStreamer< ::tensorflow::DebuggedSourceFiles,::tensorflow::EventReply>* server_unary_streamer) = 0;
  };
  typedef WithStreamedUnaryMethod_SendTracebacks<WithStreamedUnaryMethod_SendSourceFiles<Service > > StreamedUnaryService;
  typedef Service SplitStreamedService;
  typedef WithStreamedUnaryMethod_SendTracebacks<WithStreamedUnaryMethod_SendSourceFiles<Service > > StreamedService;
};

}  // namespace tensorflow


#endif  // GRPC_tensorflow_2fcore_2fdebug_2fdebug_5fservice_2eproto__INCLUDED
